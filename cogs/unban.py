from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user=None, *, reason=None):
        if reason is None:
            return await ctx.send("Veuillez indiquer une raison.")
        elif user is None:
            return await ctx.send("Veuillez indiquer un membre.")
        userName, userId = user.split("#")
        banned = await ctx.guild.bans()
        if user is None:
            return await ctx.send("Veuillez indiquer un membre.")
        for i in banned:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason=reason)
                await ctx.send(f"{user} à été dé-banni (`{reason}`).")
                return
        await ctx.reply(f"{user} n'est pas dans la liste des utilisateurs bannis.", mention_author=False)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`bannir des membres`).")


async def setup(client):
    await client.add_cog(Unban(client))
