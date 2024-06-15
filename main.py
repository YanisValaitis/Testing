import os
import time

import interactions
from interactions import SlashContext, listen, slash_command



@listen()
async def on_ready():
  print(f"We have logged in as {bot.user}")
  channel = bot.get_channel(1250791840337367061)
  await channel.send("Bot is ready for use!")



@slash_command(name="ping", description="Replies with pong!")
async def ping(ctx: SlashContext):
  await ctx.defer()
  time.sleep(5)
  await ctx.respond(content="Pong! 🏓")
  await ctx.channel.send(content=f"<@{ctx.author.id}> Hello! The bot is currently under development. If you spot any bugs or have any suggestions, please tell Yanis_Valaitis about that. Thank you!")








bot = interactions.Client(token=os.environ['TOKEN'],intents=interactions.Intents.DEFAULT)
bot.start()
