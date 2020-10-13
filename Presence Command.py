@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('🎃Prefix here dev here '))
