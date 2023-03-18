import datetime
import time

import asyncio
import discord
import json
import os
import random
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions, MissingAnyRole, CommandNotFound, CheckFailure

from tesda import datas, Opens, saves, cooldConvert

with open("config.json", "r") as f:
    config = json.load(f)

Token = config["Token"]
Prefix = config["Prefix"]
Version = config["Version"]
Goal = config["Goal"]


class Tesda(commands.Bot):
    async def setup_hook(self):
        print(f"{self.user.name} est en ligne")
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}')


intents = discord.Intents.all()
client = Tesda(command_prefix=Prefix, intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    global startTime
    startTime = time.time()
    changeStatus.start()
    setPower.start()
    print("On ready")

# Arrivées


@client.event
async def on_member_join(member):
    if member.guild.id == 991074780105015337:
        channel = member.guild.get_channel(991084100532191303)
        membre = member.guild.get_role(991114582275932170)
        await member.add_roles(membre)
    else:
        channel = member.guild.get_channel(999064286901051412)
    await channel.send(f"```yaml\n[+] {member.name}\n```")

# Départs


@client.event
async def on_member_remove(member):
    if member.guild.id == 991074780105015337:
        channel = member.guild.get_channel(991084100532191303)
    else:
        channel = member.guild.get_channel(999064308661092422)
    await channel.send(f"```yaml\n[-] {member.name}\n```")


# Change Status

@tasks.loop(seconds=5)
async def changeStatus():
    players = ["Noan", "Arthur", "Louka", "Raphaël", "Manolo", "Bastien", "Robin DuGay"]
    player = random.choice(players)
    uptimes = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
    status = ["*help", "son code", "ses modules", "tesda.json", f"la version {Version}", "l'économie", "*log",
              "Discord.py", f"l'inventaire de {player}", "Le Pangot", f"depuis {uptimes}", "*support"]
    stat = random.choice(status)
    await client.change_presence(
        activity=discord.Streaming(name=stat, url="https://twitch.tv/linca", platform="Twitch"))


# Uptime Commande

@client.command(aliases=["upt"])
async def uptime(ctx):
    uptimes = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
    await ctx.reply(f"<:Klok:1011249114807279656> {uptimes}", mention_author=False)


# Projet Colibrie Member Count & Goal


@tasks.loop(seconds=2)
async def colMemCount():
    guild = client.get_guild(991074780105015337)
    Memcount = guild.member_count
    goal = Goal
    goalPercent = Memcount * 100 / goal
    goalVoice = client.get_channel(1007339738002358383)
    voice = client.get_channel(1003368190283358258)
    await voice.edit(name=f"Membres: {Memcount}")
    await goalVoice.edit(name=f"Goal: {goal} - {goalPercent}%")

# Auto Loot System


@tasks.loop(seconds=15)
async def autol(user):
    Opens(user)
    users = datas()
    gold = random.randint(0, 1)
    copper = random.randint(0, 2)
    steel = random.randint(0, 3)
    tin = random.randint(0, 4)
    food = random.randint(0, 5)
    trash = random.randint(0, 5)

    users[str(user.id)]["gold"] += gold
    users[str(user.id)]["copper"] += copper
    users[str(user.id)]["steel"] += steel
    users[str(user.id)]["tin"] += tin
    users[str(user.id)]["food"] += food
    users[str(user.id)]["trash"] += trash

    saves(users)

# Auto Work System


@tasks.loop(seconds=15)
async def auto(user):
    Opens(user)
    users = datas()
    earn = random.randint(1, 7)
    users[str(user.id)]["bank"] += earn
    saves(users)

# On Message System


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    user = message.author
    Opens(user)
    users = datas()

    earn = random.randint(2, 7)
    xp = random.randint(1, 10)

    users[str(user.id)]["bank"] += earn
    users[str(user.id)]["msg"] += 1
    users[str(user.id)]["xp"] += xp

    lvlAmt = users[str(user.id)]["lvl"]

    nextlvl = users[str(user.id)]["lvl"] * 4 * 50

    if users[str(user.id)]["lvl"] == 0:
        return
    else:
        if users[str(user.id)]["xp"] >= nextlvl:
            await message.reply(f"Bravo {user.name}, vous êtes passé niveau {lvlAmt}.")
            users[str(user.id)]["xp"] -= nextlvl
            users[str(user.id)]["lvl"] += 1

    saves(users)

    await client.process_commands(message)

# Workers Command


@client.command()
@commands.has_any_role(1014508719985410148)
@commands.cooldown(1, 3600)
async def workers(ctx, cmd=None, arg=None):
    if cmd == "loot":
        if arg == "start":
            global wup
            wup = time.time()
            user = ctx.author
            await ctx.send("Vos ouvriers ont commencé à travailler.")
            autol.start(user)
            await asyncio.sleep(1800)
            autol.stop()
            await ctx.send("Vos ouvriers ont fini leurs travaux.")
            msg = await ctx.send(user.mention)
            await msg.delete()
    if cmd == "bank":
        if arg == "start":
            wup = time.time()
            user = ctx.author
            await ctx.send("Vos ouvriers ont commencé à travailler.")
            auto.start(user)
            await asyncio.sleep(1800)
            auto.stop()
            await ctx.send("Vos ouvriers ont fini leurs travaux.")
            msg = await ctx.send(user.mention)
            await msg.delete()
    if cmd == "stop":
        wup = time.time()
        user = ctx.author
        auto.start(user)
        autol.start(user)
        await ctx.message.delete()
        msg = await ctx.send("-")
        await msg.delete()


@workers.error
async def workers_error(ctx, error):
    if isinstance(error, MissingAnyRole):
        await ctx.send("Vous n'avez pas la permission (`être vip`).")

# Lottery command


@client.command(aliases=["lot"])
@commands.has_permissions(kick_members=True)
async def lottery(ctx):
    user = ctx.author
    Opens(user)
    users = datas()
    lots = [10, 15, 50, 100, 150, 175, 250, 500, 700, 1000]

    msg = await ctx.reply("Veuillez envoyer la commande ci dessous (*Sans espace, ni majuscule.*)\n```yaml\nmoi\n```")

    players = []

    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

    try:
        while True:
            participation = await client.wait_for('message', timeout=10, check=check)
            players.append(participation.author)
            await msg.reply(f"{participation.author.name} participe au tirage.")
    except:
        print(".")

    await ctx.send("<a:loading:1000544602081734726> Le tirage va commencer...")
    await asyncio.sleep(3)
    winner = random.choice(players)
    price = random.choice(lots)
    users[str(user.id)]["bank"] += price

    saves(user)

    await ctx.send(f"{winner.name} a gagné(e) {price}€ <a:tada:1001489515225026630>")


@lottery.error
async def lottery_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Vous n'avez pas la permission (`gérer les messages`).")

# Change Nickname


@client.command()
async def chnick(ctx, member: discord.Member, nick=None):
    await member.edit(nick=nick)
    await ctx.send(f'Le surnom à été changé pour {member.mention}')

# On Command Error


# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         await ctx.reply(
#            f"<:cooldown:1011248209739382824> Veuillez recommencer dans {cooldConvert(round(error.retry_after, 2))}", mention_author=False)
#     if isinstance(error, CommandNotFound):
#         await ctx.reply(
#             f"<:no:1002224555798044672> *Scheisse !* Commande inconnue", mention_author=False
#         )
#     if isinstance(error, CheckFailure):
#         await ctx.reply(
#             f"<:no:1002224555798044672> *Scheisse !* Cette commande sera disponible avec la v3.0.0", mention_author=False
#         )


@client.command()
async def wup(ctx):
    wuptime = str(datetime.timedelta(seconds=int(round(time.time() - wup))))
    await ctx.reply(f"<:Klok:1011249114807279656> {wuptime}", mention_author=False)


@client.command()
async def release(ctx):
    await ctx.send("Release <:Py2:1010607171794391040> Tesda v3.0.0:\nhttps://discord.gg/KNuaVx4j?event=1011599280219369472\n\nVoici les commandes bientôt disponible :\n• `pay`\n• `bounty`\n• `shifoumi`\n• `tag`\n• `ticket`")


@tasks.loop(seconds=5)
async def setPower():
    guild = client.get_guild(991074780105015337)
    for member in guild.members:
        if member.id == client.user.id:
            pass
        if member.bot is True:
            pass
        else:
            user = member
            Opens(user)
            users = datas()
            message = users[str(user.id)]["msg"]
            power = message / 100
            users[str(user.id)]["power"] = power
            saves(users)


@client.command()
async def power(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    users = datas()
    await ctx.reply(f"La Power <:power:1011994788452638751> de {user.name} est de **{users[str(user.id)]['power']}** <:power:1011994788452638751>", mention_author=False)


client.run(Token)
