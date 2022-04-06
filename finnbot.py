"""
Welcome to the jungle bitch
"""

import discord
import requests
import json
from tayk import *

token = 'NzgxMjkxNDE3MjA5Mjc0Mzg4.X77gVQ.U_A7HP5-42LfK_GaEJbd5D0vcGw'
client = discord.Client()

#Commands
command_prefix = '/'
roast_command = command_prefix + 'roast_finn'
compliment_command = command_prefix + 'compliment_sabrina'
kanye_command = command_prefix + 'kanye_quote'
bars_command = command_prefix + 'drop_some_bars'
tayk_command = command_prefix + 'tay_k'

#APIs
api_url = 'https://api.snowflakedev.xyz/roast'
kanye_url = 'https://api.kanye.rest/'
bars_url = 'https://a3odwonexi.execute-api.us-east-2.amazonaws.com/default/Bars_API'

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name='Incinerating Finn'))


@client.event
async def on_message(message):
	if not message.author.bot:
		if message.content == roast_command:
			data = requests.get(api_url).content.decode()
			roast = json.loads(data)['roast']
			roast = "Dear Finn, " + roast
			await message.channel.send(roast)
		if message.content == compliment_command:
			compliment = "Sabrina is super cool and nice and cool"
			await message.channel.send(compliment)
		if message.content == kanye_command:
			data = requests.get(kanye_url).content.decode()
			quote = json.loads(data)['quote']
			await message.channel.send(quote)
		if message.content == bars_command:
			data = requests.get(bars_url).content.decode()
			bars = json.loads(data)['data']
			await message.channel.send(bars)
		if message.content == tayk_command:
			taykay = tayk()
			await message.channel.send(taykay)


client.run(token)
