import os
import discord
from dotenv import load_dotenv
from discord.client import Client
from discord.flags import Intents
from discord.message import Message
from discord.ext import commands,tasks

from openai_api.openapi_connector import get_chat_gpt_response

load_dotenv()

intents = discord.Intents.default()
intents.presences = True
intents.messages = True
intents.guilds = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot_caller: str = "Gengar"

discord_token = os.environ.get("DISCORD_TOKEN")

class CustomDiscordClient(Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="!help for commands"), status=discord.Status.dnd)
        print(f"Estou conectado ao Discord com o user {self.user}")
    
    async def on_message(self, message: Message):
        # Check if the message is from the bot itself
        if message.author == custom_discord_client.user:
            return  # Ignore messages from the bot itself

        # Convert both the message content and the bot_caller to lowercase
        lowercase_message = message.content.lower()
        lowercase_bot_caller = bot_caller.lower()

        # Check if the lowercase message contains the lowercase keyword
        if lowercase_bot_caller in lowercase_message:
            # Extract the prompt without the prefix
            prompt: str = message.content[len(bot_caller):].strip()
            print(f"---------- Prompt message: {prompt} ----------")
            chat_gpt_response: str = get_chat_gpt_response(question=prompt)
            if chat_gpt_response:
                await message.channel.send(content=chat_gpt_response)

intents = Intents.default()
intents.message_content = True
custom_discord_client: CustomDiscordClient = CustomDiscordClient(intents=intents)
