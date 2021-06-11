import discord
import random

from databaseconfig import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return
    
    if message.channel.name == '💬chat💬':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Goodbye {username}, have a wonderful rest of your day!')
            return
        elif user_message.lower() == '!random':
            res = f"Calculating...\nYour random number is: {random.randrange(1000000)}"
            await message.channel.send(res)
        elif user_message.lower() == 'how are you doing today':
            await message.channel.send(f'I am doing great today thank you for asking! How are you doing {username}?')
            return
        elif user_message.lower() == 'do you know any jokes?':
            await message.channel.send("Why did the hipster burn his mouth? He drank the coffee before it was cool!")
            return
        elif user_message.lower() == 'tell me something funny':
            await message.channel.send("What did the buffalo say when his son left for college? Bison")
            return
        elif user_message.lower() == 'Whats up?':
            await message.channel.send('The sky')
            return
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return


client.run(TOKEN)