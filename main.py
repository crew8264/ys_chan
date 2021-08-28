import discord
from discord.ext import commands

app = commands.Bot(command_prefix='/')

# @  : 데코레이터 라고 함.
#    : 함수를 인자로 받아, 코드 중간에 func()로 함수 실행.



# 이벤트
@app.event
async def on_ready():
    print('자 이제 시작해볼까, 준비는 됐어 ? ')
    # print(app.user.name, end = "")
    print('좋아, 성공적으로 연결되었어 >< ')
    await app.change_presence(status=discord.Status.online, activity=None)

    
# 임베드
embed = discord.Embed(title='노티쨩?',description='등장해줘-☆', color = 0x00ff00)
embed.add_field(name='주의하라구- : ',value='지금부터는 약속이니까 말이야!!', inline=True)
# embed.set_image(url='url')
# embed.set_thumbnail(url='url')
# embed.set_footer(text='footer text',image_url='this is option')

# await ctx.send(embed=embed(emb01))


# 명령어
@app.command()
async def 안녕(ctx):
    await ctx.send('안녕 안녕 오늘도 죠은 하루야 칭구 ><')
    await ctx.send(embed=embed)

@app.command()
async def 소환(ctx):
    await ctx.send('안녕 안녕 오늘도 죠은 하루야 칭구 ><')

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
app.run('ODgxMDg1MzA2MTQ3ODQ4MjAy.YSnsog.HB7R_fc-TTepbmGbirrHZhN5h90')
