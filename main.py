import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for $cmd - Cussing into a microphone"))
  print('Bot Status Success.')
  print('We have logged in as {0.user}'.format(client))
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
  
    if message.content.startswith('$archive'):
      await message.channel.send('https://www.wobbly-tooth-archive.xyz/')

    if message.content.startswith('$1v1'):
      await message.channel.send('***Kills you with a crossbow***')

    if message.content.startswith('$twitter'):
      await message.channel.send('https://twitter.com/WobblyToothLtd')

    if message.content.startswith('$cmd'):
      await message.channel.send('Put a **$** infront of each word/phrase. `| help | cmd | archive | 1v1 | twitter | legend | tranq | crossbow | tip | clans | war | hack | auth | lewd | cheat | kill | question | rp | pedo | tyler | shotgun | knife | pistol |`')

    if message.content.startswith('$legend'):
      await message.channel.send('A legend defined by the Urban Dictionary is anybody besides JokerPGM.')

    if message.content.startswith('$tranq'):
      await message.channel.send('A Tranq is an weapon that most PVPers used, from late 2018 - Present. You can use the rapid fire glitch to kill people really fast. This weapon does the second most damage in the game at 25 damage. And can be expanded to 125 damage per shot with the neck damage glitch. https://www.models-resource.com/resources/big_icons/19/18172.png')

    if message.content.startswith('$crossbow'):
      await message.channel.send('A crossbow is an weapon that does 10 damage. This is the slowest and most quiet weapon. But can be a pain in the butt to deal with when theirs a sniper in all white. *Orange* https://www.models-resource.com/resources/big_icons/19/18165.png')

    if message.content.startswith('$tip'):
      await message.channel.send('Get good red-coat.')

    if message.content.startswith('$clans'):
      await message.channel.send('Clans are just a bullshit way to give individual users power over other individuals who have no following. Normally clan leaders are sad ass 14 year olds who crave attention fyi.')

    if message.content.startswith('$war'):
      await message.channel.send('You wish there was a "clan-war". The only war that lasted longer than a week, was the devorce between me and your mom.')

    if message.content.startswith('$hack'):
      await message.channel.send('And that was the final nail in the coffin.')

    if message.content.startswith('$auth'):
      await message.channel.send('The bot was authorized via: Discord:tm:')

    if message.content.startswith('$lewd'):
      await message.channel.send('Horny fucks like you thought this command was going to give some Ice Station Z R34. You thought wrong buddy, now here is a stock image of a sad dog for you: https://thumbs.dreamstime.com/z/sad-dog-laying-floor-32915662.jpg')

    if message.content.startswith('$kill'):
      await message.channel.send('You died after being captured by the rip-off version of Order66.')

    if message.content.startswith('$cheat'):
      await message.channel.send('You think I would give you a cheat to destroy the game? Well you are right, I would, I would if I was a degenerate who had no fucking life. Get good r*tard.')

    if message.content.startswith('$rp'):
      await message.channel.send('UwU... **I will take a shit on your face if you make me do that fucking weird ass thing again.**')

    if message.content.startswith('$question'):
      await message.channel.send('When will you get an actual girl-friend? It seems like you havent gotten one that isnt a catfish yet.')

    if message.content.startswith('$pedo'):
      await message.channel.send('Get the fuck away from me!')

    if message.content.startswith('$tyler'):
      await message.channel.send('...')

    if message.content.startswith('$shotgun'):
      await message.channel.send('A absolute classic PVP weapon. Its easy to find. Can fire long ranges. And does the third most damage in the game. Next to the tranquilizer. https://www.models-resource.com/resources/big_icons/19/18170.png')

    if message.content.startswith('$pistol'):
      await message.channel.send('A weapon that has four shots and very fast. Good for taking out a few Zombies at a time. https://www.models-resource.com/resources/big_icons/19/18169.png')

    if message.content.startswith('$knife'):
      await message.channel.send('A weapon that used to be popular amongst new players. Now it is resided by hackers. Nobody can escape you when you attack with this monstrosity. https://www.models-resource.com/resources/big_icons/19/18168.png')

    if message.content.startswith('$help'):
      await message.channel.send('So if you are really that much of a dumb-ass, that did **not** look at my status. And if you must know, use **$cmd** for my commands. And use **$** infront of every word. Because lets be honest, who the fuck asks a bot for help?')

keep_alive()
client.run(os.getenv('TOKEN'))
