import discord
client = discord.Client(intents=discord.Intents.default())

token="MTE1NTA4MjA3NzI0NzY0MzcyOA.GvoA8I.24y6_lzOZZmqkmzikS2_nMMyBGpt7JYtmRJrTM"
@client.event
async def on_Ready():
    print("We have logged in as {0.user}").format(client)

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith("!help"):
        await message.channel.send("Commands: \n !csv - get the csv file the livescores are stored in \n !livescore - get the live scores")
    elif message.content.startswith("!livescore"):
        await message.channel.send("This feature will be available soon .")
    elif message.content.startswith("!csv"):
        await message.channel.send("This feature will be available soon .")
    else:
        await message.channel.send("featured topic not in domain  , please give a proper function . ")
client.run(token)