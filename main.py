# credit to https://betterprogramming.pub/coding-a-discord-bot-with-python-64da9d6cade7 for providing the information on how to do this bot.
# I have adapted it since to specify my needs. Was a great start.
import os
import random
import discord

token = os.environ["token"]
url = "https://discord.com/api/oauth2/authorize?client_id=971015548932599808&permissions=2048&scope=bot"
client = discord.Client()

quote_list = ["Look at me, I'm a cat",
			  "I look the concern",
			  "WITNESS ME",
			  "NO PETS, ONLY CONCERN,",
			  "Come with me and I show you grass",
			  "Stay Hydrated",
			  "CEASE DRINKING THE CAFFEINE, PEACH WILLS IT"]

key_word_list = ["hello peach",
				 "peach",
				 "cat",
				 "bastard"]

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY SERVERS THE BOT IS IN.
	print("Bot is in " + str(guild_count) + " servers.")

@client.event
async def on_message(message):
# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO A LIST ITEM FROM KEYS WORDS.
	if message.content.lower() in key_word_list:
		# SENDS BACK A CAT TO THE CHANNEL FROM A LIST USING A RANDOM NUMBER BASED ON LENGTH OF LISTS.
		peach_number = random.randint(0, len(os.listdir("images")))
		quote_number = random.randint(0, (len(quote_list)))
		await message.channel.send(file=discord.File(f"images/peach{peach_number}.jpeg"))
		await message.channel.send(quote_list[(random.randint(0,quote_number))])
		#CODE BELOW FOR TESTING NUMBERS
		#await message.channel.send(f"{peach_number}, {quote_number}")


client.run(token)