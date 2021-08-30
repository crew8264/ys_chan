import discord, asyncio
from func_excp import *
from discord.ext import commands
#from openpyxl import Workbook

app = commands.Bot(command_prefix='/')

# @  : 데코레이터 라고 함.
#    : 함수를 인자로 받아, 코드 중간에 func()로 함수 실행.

print('자 이제 시작해볼까, 준비는 됐어 ? ')

# 이벤트
@app.event
async def on_ready():
    # print(app.user.name, end = "")
    print('좋아, 성공적으로 연결되었어 >< ')
    await app.change_presence(status=discord.Status.online, activity=discord.Game("나 바쁘니까 건들지 마 ㅡ"))


# 임베드

# 노티쨩 ---
noti = discord.Embed(title='노티쨩 ?', description='이리와봐ㅡㅡ', color = 0xd756a3)
noti.add_field(name='이상 주의하라구- : ', value='쉽게 무시해서는 안될꺼시야!!', inline=True)
# embed.set_image(url='url')
# embed.set_thumbnail(url='url')
# embed.set_footer(text='footer text',image_url='this is option')
# await ctx.send(embed=embed(emb01))

# 헬프쨩 ---
helpi = discord.Embed(title='헬프쨩 -', description='나와서 애 좀 처리해줘. 난 바빠서 이만- ', color = 0x68d182)
help = discord.Embed(title='이하 헬프쨩 등쟝 ><', description='저는 이런 말을 할 수 있어요 !!', color = 0xd756a3)
#help.add_field(name='이하 헬프쨩 등쟝 ><', value='저는 이런 말을 할 수 있어요 !!', inline=False)
help.add_field(name='안녕', value='인사해주는 것 뿐이에요... 아쉬우신가요?', inline=False)
help.add_field(name='소환', value='조금 다르게 인사해보는거에요 ><', inline=False)
help.add_field(name='도움', value='제가 할 줄 아는 말을 볼 수 있어요 !!', inline=False)
help.add_field(name='멘션', value='(@대상) 어떤 유저에게 멘션을 넣을 수 있답니다.', inline=False)
help.add_field(name='따라해봐', value='(대화) 당신의 말을 따라할 수 있답니다 ><', inline=False)
help.add_field(name='바보', value='(@대상) 여신쨩이 뒷골목으로 데리고 들어갈 지도 몰라요... 전 너무 무서운걸요 !!', inline=False)



# 앱 동작 범위
@app.event
async def on_error(event, *args, **kwargs):
    print("나 뻗을꺼야...꽥;")

@app.event
async def on_command_error(ctx, error):
    await ctx.send('채팅도 똑바로 못치는거야?')
    await ctx.send('정신 차리라구 ㅡㅡ')
    print(error)

@app.event
async def on_member_join(member):
    print(member + "니가 새로 참여한 칭구구나? 다시 나가라구 ㅡㅡ")


# 주워온 코드
@app.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await ctx.send("흥 안녕 안해줄껀데에 ㅡ")
            break


@app.event
# 메시지가 들어 올 때마다 가동되는 구문
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("/도움"):
        await message.channel.send('도움이 필요하댜구?')
        await message.channel.send('귀찮게 또 이야기 해야하냐구ㅡㅡ')
        await message.channel.send(embed=helpi)
        await message.channel.send(embed=help)
        return

    await app.process_commands(message)


# 명령어
@app.command()
async def 안녕(ctx):
    await ctx.send('인사 시키지마. 하나도 재미 없거든 ㅡ')
    await ctx.send(embed=noti)

@app.command()
async def 소환(ctx):
    await ctx.send('또 부르지 말라구 ㅡㅡ /귀환')

@app.command()
async def 도움(ctx):
    pass

@app.command()
async def 멘션(ctx, user: discord.User):
    await ctx.send("{}님?".format(user.mention))
    if checkName(user.name, user.id):
        await ctx.send("이 값은 트루 값이야.")
    else:
        await ctx.send("뭐 어쩌라구, 그냥 불러봤는뎅-")

@app.command()
async def 바보(ctx, user_name: discord.Member):
    await ctx.send('너 거기 딱기다려...?')
    channel = await user_name.create_dm()
    await channel.send("좋은 말 할때 그만두는게 좋아.")
    await channel.send("한번만 더 그런 채팅 치면 혼낼꺼라구-")
    await ctx.send('흥 혼내줘버렸어.')
    
    

# 명령어 뒤에있는 단어를 모두다 파라미터에.
@app.command()
async def 따라해봐(ctx, *, text):
    await ctx.send(text)

# 첫번째 파라미터만 받는.
@app.command()
async def 따라해봐2(ctx, text):
    await ctx.send(text)

# 리스트 ( 배열)로 하는건데 파라미터 앞에 *을 붙이면, 배열로 인식을 해서
# ['안녕하세요,','명이입니다.']
# 그래서, for문을 이용해서 붙이는.
@app.command()
async def 따라해봐3(ctx, *text):
    txt = ''
    for tmp in text:
        txt += tmp
        txt += ', '
    await ctx.send(txt[:-2])



# 앱 동작 토큰
token = open("token", "r").readline()
bot.run(token)
