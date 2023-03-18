from discord.ext import commands


class Tag(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tag(self, ctx, tag=None):
        user = ctx.author
        cmd = [
            {"name": "tesda", "content": "<:Py2:1010607171794391040> **Tesda.pyw**\n\n*Créateur*: Nøanh07_\n*Nationalité*: <:flag:1009135146420670525> Français\n*Nombre de Commande*: <:counter:1011331854000984114> `43` Commande(s)"},
            {"name": "discord.py", "content": "<:python:1010543599961784370> **Discord.py**\n\nDiscord.py est un module *Python*, créer en 2015 par __Rapptz__.\nUtilisé pur créer des bots Discord, il comporte beaucoup de *Features*:\n-> API moderne utilisant `async` & `await`,\n-> Optimisé pour la vitesse & la mémoire,\n-> Facile à utiliser avec une conception orientée objet.\n-> Documentation: https://discordpy.readthedocs.io/en/stable/api.html"},
            {"name": "advancedlogging", "content": "<:python:1010543599961784370> **Advanced Logging**\n\nVoici un *Advanced Logging* que j'utilise:\n```py\nclass Tesda(commands.Bot):\n    async def setup_hook(self):\n        print(f'{self.user.name} est en ligne')\n        for filename in os.listdir('cogs'):\n            if filename.endswith('.py'):\n                await client.load_extension(f'cogs.{filename[:-3]}')\n\n\nintents = discord.Intents.all()\nclient = Tesda(command_prefix=Prefix, intents=intents)\nclient.remove_command('help')\n\nclient.run(Token)```"},
            {"name": "advLog", "content": "<:python:1010543599961784370> **Advanced Logging**\n\nVoici un *Advanced Logging* que j'utilise:\n```py\nclass Tesda(commands.Bot):\n    async def setup_hook(self):\n        print(f'{self.user.name} est en ligne')\n        for filename in os.listdir('cogs'):\n            if filename.endswith('.py'):\n                await client.load_extension(f'cogs.{filename[:-3]}')\n\n\nintents = discord.Intents.all()\nclient = Tesda(command_prefix=Prefix, intents=intents)\nclient.remove_command('help')\n\nclient.run(Token)```"},
            {"name": "cogs", "content": "<:Py2:1010607171794391040> **Cogs**\n\nVoici un cogs (extension du `main.py`):\n```py\n# Par exemple un ban.py\nfrom discord.ext import commands\n\nclass Ban(commands.Cog):\n    def __init__(self, client):\n        self.client = client\n\n# Ton code ici\n\nasync def setup(client):\n    await client.add_cog(Ban(client))\n```"},
            {"name": "uptime", "content": "<:Py2:1010607171794391040> **Uptime Commande**\n\nLa commande *uptime* (voir depuis combien temps le bot est allumé)\n```py\nimport datetime\n\n@client.event\nasync def on_ready():\n    global startTime\n    startTime = time.time()\n\n@client.command(aliases=['upt'])\nasync def uptime(ctx):\n    uptimes = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))\n    await ctx.reply(f'<:Klok:1011249114807279656> {uptimes}', mention_author=False)\n```"},
            # {"name": "cooldown", "content": "<:Py2:1010607171794391040> **Cooldown**\n\nVoici comment faire un cooldown avec D.py:\n```py\nfrom discord.ext import commands\n\n@client.command()\n@commands.cooldown(1, 120)\nasync def cooldown(ctx)\n    await ctx.send('Voici un exemple')\n```"},
            {"name": "bounty", "content": "**Bounty**\n\nEnsemble de commande\n->`bounty set <user> [amount]`\n->`bounty catch <user>`\n-> système de power (message hebdo / 10)"},
            {"name": "json", "content": "**Fichier Json**\n\nVoici la dernière save du fichier json de tesda:\n{'439743312413458432': {'bank': 2439692, 'msg': 439, 'xp': 453, 'lvl': 5, 'warn': 0, 'power': 4.39, 'bounty': 105000, 'gold': 263, 'copper': 535, 'steel': 844, 'tin': 1076, 'food': 1261, 'trash': 1287}"}
        ]
        if tag is None:
            return await ctx.reply("Veuillez indiquer un *Tag*.", mention_author=False)
        else:
            if tag is not None:
                for i in cmd:
                    name = i["name"]
                    content = i["content"]
                    if tag == name:
                        await ctx.reply(content, mention_author=False)
            else:
                await ctx.reply("Tag non reconnue", mention_author=False)


async def setup(client):
    await client.add_cog(Tag(client))
