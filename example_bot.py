import os
import discord
from markov import open_and_read_file, make_chains, make_text

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping_irynas_bot'): # trigger phrase
        # await message.channel.send('Hello!')
        input_path = 'green-eggs.txt'
        # Open the file and turn it into one long string
        input_text = open_and_read_file(input_path)
        # Get a Markov chain
        chains = make_chains(input_text)

        # Produce random text
        random_text = make_text(chains)

        await message.channel.send(random_text)

client.run(os.environ['DISCORD_TOKEN'])
