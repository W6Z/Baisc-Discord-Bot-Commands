
@client.event
async def on_message(message):
    if message.content.startswith('message here'):
        myMsg = await myMsg.send('*message* delete_after=8)
        await myMsg.add_reaction("emoji here)
        await myMsg.add_reaction("emoji here)
        
 
