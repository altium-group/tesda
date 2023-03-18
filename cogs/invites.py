from discord.ext import commands
import discord
from tesda import isOwner


class Invites(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(isOwner)
    async def invites(ctx, user: discord.Member = None):
        isInRelease = True
        if user is None:
            totalInvites = 0
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    totalInvites += i.uses
            await ctx.send(f"Vous avez invité {totalInvites} membre{'' if totalInvites == 1 else 's'}")
        else:
            totalInvites = 0
            for i in await ctx.guild.invites():
                if i.inviter == user:
                    totalInvites += i.uses
                await ctx.send(f"{user.name} a invité {totalInvites} membre{'' if totalInvites == 1 else 's'}")


async def setup(client):
    await client.add_cog(Invites(client))
