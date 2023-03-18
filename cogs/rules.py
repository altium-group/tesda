from discord.ext import commands
import discord, datetime
from discord.ext.commands import MissingAnyRole


class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(999065641279557652)
    async def rules(self, ctx):
        Channel = ctx.guild.get_channel(999292002451607562)
        Text = discord.Embed(title="<:rules:1009135151353180281> Règle de Support - Tesda",
                             description="• Pas de spam,\n• Pas de flood,\n• Pas d'insulte,\n• Pas de propos racistes,\n• Autopromotion interdite.")
        times = datetime.datetime.now()
        Text.set_thumbnail(url="https://cdn.discordapp.com/emojis/1009135146420670525.png")
        Text.set_footer(text=f"Tesda • {times.day}/{times.month}/{times.year}", icon_url=ctx.guild.icon)
        await Channel.send(embed=Text)
        await Channel.send(
            "Veuillez envoyer la commande ci dessous (*Sans espace, ni majuscule.*)\n```yaml\n*join\n```")

    @rules.error
    async def rules_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.send("Vous n'avez pas la permission (`être Super-Modérateur`).")


async def setup(client):
    await client.add_cog(Rules(client))
