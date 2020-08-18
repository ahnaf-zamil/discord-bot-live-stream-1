import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        if member:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked **{member}**")
        else:
            await ctx.send(f"**{ctx.message.author}**, Who do you want me to kick?")


    @commands.command()
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        if member:
            await member.ban(reason=reason)
            await ctx.send(f"Banned **{member}**")
        else:
            await ctx.send(f"**{ctx.message.author}**, Who do you want me to ban?")

    @commands.command()
    async def unban(self, ctx, *, member):
        if member:
            banned_members = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")

            for ban_entry in banned_members:
                user = ban_entry.user

                if (user.name, user.discriminator) == (
                    member_name,
                    member_discriminator,
                ):
                    embed = discord.Embed(
                        title="Unbanned",
                        color=discord.Color.blue(),
                        description=f"{member} was unbanned by {ctx.message.author.mention}.",
                    )
                    await ctx.send(embed=embed)
                    await ctx.guild.unban(user)
                   
                    return
        else:
            await ctx.send(f"Who do you want to unban {ctx.message.author.mention}?")

def setup(bot):
    bot.add_cog(Moderation(bot))