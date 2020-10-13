@client.event
async def on_member_join(member):
    c = member.guild.system_channel
    if c:
        await c.send(f"Welcome to the server, {member.mention}")
