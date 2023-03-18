from discord.ext import commands
import random


class Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def ball(self, ctx):
        answers = [
            "Oui", "Non", "Pourquoi pas", "Peut-être", "Hmm", "pas sûr de ça...", "Ca m'offense", "ptdr",
            ":thinking:", "<a:awarn:1001489503887835317> Vous avez été warn pour, Propos choquant/raciste."
        ]
        result = random.choice(answers)
        await ctx.send(result)


async def setup(client):
    await client.add_cog(Ball(client))
