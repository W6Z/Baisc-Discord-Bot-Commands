@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == '704785522484183172':
        role = discord.utils.get(member.add_roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)
