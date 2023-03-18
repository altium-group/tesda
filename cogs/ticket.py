from discord.ext import commands
import json, discord
from tesda import isOwner


class Tickets(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ticket(self, ctx, cmd=None):
        with open("config.json", "r") as f:
            config = json.load(f)
            Count = config["count"]
        if cmd is None:
            return await ctx.send("Veuillez indiquer une action.")
        elif cmd == "create":
            await ctx.message.delete()
            if ctx.channel.id != 1011368586880757781:
                return await ctx.send("Veuillez vous rendre dans <#1011368586880757781>")
            else:
                name = "🍀 | Tickets"
                category = discord.utils.get(ctx.guild.categories, name=name)
                support = ctx.guild.get_role(1011385778183610498)
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                    ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True)
                }
                channel = await ctx.guild.create_text_channel(name=f"Ticket-{'00' if Count <= 9 else '0'}{Count}", category=category, overwrites=overwrites)
                config["count"] += 1
                await channel.send(f"<:Fr:1011384095420453016> Bienvenue, tu peut poser tes questions ici. Quand tu auras fini, ferme le ticket avec `ticket close`.\n<:Usa:1011384092618670180> Welcome, you can ask question here. When you have finished, close the ticket with `ticket close`.\n{ctx.author.mention}")
                with open("config.json", "w") as f:
                    json.dump(config, f)
        elif cmd == "msg":
            await ctx.message.delete()
            if ctx.channel.id != 1011368586880757781:
                return await ctx.send("Veuillez vous rendre dans <#1011368586880757781>")
            else:
                await ctx.send("<:Py2:1010607171794391040> *Système de Tickets*\nVeuillez envoyé la commande ci-dessous pour créer un ticket d'aide.\n```yaml\n*ticket create\n```")
        elif cmd == "close":
            await ctx.channel.delete(reason="Ticket fermé")


async def setup(client):
    await client.add_cog(Tickets(client))
