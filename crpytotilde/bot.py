import discord
import discord.member
import json
from discord import member
from discord.ext import commands
from discord.utils import get




client = discord.Client()
client = commands.Bot(command_prefix='-')



@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='To Mysterious Convos'))
print('We have logged in as {0.user}'.format(client))



@client.command()
async def getclue(ctx):
    await ctx.send('The clues for this month can be found at "https://tildethine.xyz/mysteryclue1"')

 #helpdashboard
@client.command()
async def ineedhelp(ctx):
    embed = discord.Embed(
        title="Help Dashboard",
        url="https://reddit.com/r/tildethine",
        description="**Below are some commands you can use with the bot. Prefix is -**", color=0xFF5733)
    embed.add_field(name="**earntildes**", value="Lists a few ways on how you can earn some Tildes.", inline=False)
    embed.add_field(name="**socials**", value="Displays our socials, Twitter ect.", inline=False)
    embed.add_field(name="**getclue**", value="Displays the clue for the current month.", inline=False)
    embed.add_field(name="**saveaddress**", value="Saves your stellar address for easy access with the command `showaddress`", inline=False)
    embed.add_field(name="**contract**", value="Asset info.", inline=False)
    await ctx.send(embed=embed)

#addresssave
@client.command()
async def saveaddress(ctx):
    # Since bot asks the user the address seperately we don't need to accept any arguments.
    await ctx.send("Enter your address here")
    msg = await client.wait_for(
        "message",
        check=lambda msg: msg.channel.id == ctx.channel.id
        and msg.author.id == ctx.author.id,

    )
    # msg.content now contains the address
    # we write it to an json file, I recommend using a postgres db for this if this is for serious use
    with open("data.json") as r:
        data = json.load(r)
    with open("data.json", "w+") as w:
        data[str(ctx.author.id)] = msg.content
        w.write(json.dumps(data))
    await ctx.send("Successfully assigned address")


@client.command()
async def showaddress(ctx):
    # OP of the stack post did not mention if this should take any arguments
    # So this doesn't take args and just displays invoke user's address
    with open("data.json") as r:
        data = json.load(r)
    await ctx.send("\n{}".format(data[str(ctx.author.id)]))



#contract, asset address and issuer and code

@client.command()
async def contract(ctx):
    embed = discord.Embed(
        title="Contract",
        url="https://reddit.com/r/tildethine",
        description="**Stuff you need to add TildeThine as an asset**", color=0xFF5733)
    embed.add_field(name="**Asset Code**", value="TILDETHINE", inline=False)
    embed.add_field(name="**Asset Issuer**", value="GD4PRUR5HRCIBB3JVGDA5XWISOTD2YGY2ZYOWDONOK4SDYX5MIT4URUN", inline=False)
    await ctx.send(embed=embed)


#socials command
@client.command()
async def socials(ctx):
    embed = discord.Embed(
        title="Our Socials!",
        url="https://tildethine.xyz/-",
        description="Stay mysterious",
        color=discord.Color.dark_blue())
    embed.set_author(name="TildeThine", url="https://media.discordapp.net/attachments/923637570007609356/926417296459726858/tildethinelogo.png?width=364&height=417",
                     icon_url="https://media.discordapp.net/attachments/923637570007609356/926417296459726858/tildethinelogo.png?width=364&height=417")
    # embed.set_author(name=ctx.author.display_name, url="https://media.discordapp.net/attachments/923637570007609356/926417296459726858/tildethinelogo.png?width=364&height=417", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/923637570007609356/926417296459726858/tildethinelogo.png?width=364&height=417")
    embed.add_field(name="**Website**", value="https://tildethine.xyz/-", inline=False)
    embed.add_field(name="**Reddit**", value="https://reddit.com/r/tildethine", inline=False)
    embed.add_field(name="**Instagram**", value="https://instagram.com/tildethine/", inline=False)
    embed.add_field(name="**Twitter**", value="https://twitter.com/tildethinecoin/", inline=False)
    await ctx.send(embed=embed)

#trustline command
@client.command()
async def trustlinehelp(ctx):
    embed = discord.Embed(
        title="How to add a trustline",
        url="https://discord.com/channels/917389836032307290/924717827057942571/924831012972789880",
        description="Go to #creating-to-add-a-trustline or click the title to learn how!", color=0xFF5733)
    await ctx.send(embed=embed)

#earntildes command
@client.command()
async def earntildes(ctx):
    embed = discord.Embed(
        title="How to earn Tildes",
        url="https://reddit.com/r/tildethine",
        description="**There are many ways to earn some Tildes. Here is a list**", color=0xFF5733)
    embed.add_field(name="**Invite Awards**", value="Want to earn some Tildes while helping the server grow? Type '-invitewards' to learn more.", inline=False)
    embed.add_field(name="**Counting**", value="An easy way to earn Tildes. Simply join us in #counting and you can get tipped weekly if you are a top counter!", inline=False)
    embed.add_field(name="**Post Memes**", value="Post your tip-worthy memes over at r/tildethine and the community may tip you via the tipbot! Don't forget to tip others as well.", inline=False)
    embed.add_field(name="**Beg for Tildes**", value="Try your luck and beg like others in #tips-and-begging and someone might just tip you!", inline=False)
    await ctx.send(embed=embed)

#basic coin help
@client.command()
async def stellarhelp(ctx):
    embed = discord.Embed(
        title="Stellar Help",
        url="https://reddit.com/r/tildethine",
        description="**A list of common problems in stellar itself**", color=0xFF5733)
    embed.add_field(name="**Adding a trustline**", value="Use '-trustlinehelp to get info on how to add TildeThine as a trustline.", inline=False)
    embed.add_field(name="**Random Pending Coin**", value="Do not accept these coins, they have a risk of emptying your wallet and they are worthless. Your 10 seconds is worth more than these coins.", inline=False)
    embed.add_field(name="**-**", value="-", inline=False)
    embed.add_field(name="**-**", value="-", inline=False)
    await ctx.send(embed=embed)


#invite awards command
@client.command()
async def inviteawards(ctx):
    embed = discord.Embed(
        title="**Invite Awards**",
        url="https://reddit.com/r/tildethine",
        description="Want to earn some Tildes and help the server grow at the same time? Check out #inviteawards. You can get 1,000 Tildes for every human invited! Simply create an invite link to get started right away!", color=0xFF5733)
    await ctx.send(embed=embed)


#dm command
@client.command()
async def submitclue(ctx):
     def check(m):
         return m.author == ctx.author
     await ctx.send(f"{ctx.author.mention}Check your dms!")
     await ctx.author.send('Enter your answer here, all lowercase without spaces. Do not reveal this to anyone else if you got it right, everyone who solves it gets a special role and a NFT for verification purposes.')
     message = await client.wait_for('message', timeout=500, check=check)
     print(f"{message.author} is an author of the message.")
     if message.content == 'twopeople':
         member = ctx.author
         role = discord.utils.get(member.guild.roles, name="Mystery Solver 1")
         await member.add_roles(role)
         await ctx.send(f"{ctx.author.mention}Congratulations! you got it right, but it does not end here. You have been given a special role which can be used to access a secret channel in the server. The mystery will follow you there.")
     else:
         await ctx.send(f"{ctx.author.mention}Try again ;)")

client.run('OTI2MTQzNDAxMzc4ODczMzU0.Yc3YQQ.mzraDGHdxFoZwrF6dr7aSi9UEtc')



