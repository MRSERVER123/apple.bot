import discord

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('apple.net')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("/출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0x80E12A)
                channel = 953640526526173195
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MjZfMjk5%2FMDAxNjIyMDM2NzkyNTky.t0a6wR-ezZA_CnWhTyyKef3XV60SFR4Qt71sB5-BfVUg.fxiCGr5TSn_FzV52md-c1H3ODNW9JKqBHBPmG3zWrcog.JPEG.sj330035%2F%25B0%25F8%25B0%25A8.jpg&type=sc960_832")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("/퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                author = message.guild.get_member(int(message.author.id))
                embed = discord.Embed(color=0xFF0000)
                channel = 953640526526173195
                embed.set_author(name=author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fimage.nmv.naver.net%2Fcafe_2021_06_22_1207%2F5ae4b9ad-d322-11eb-90b5-505dac8c3607_01.jpg&type=a340")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run('OTUzNjMyODUwMzY2ODQ5MTE2.YjHZzQ.Qw2ksGiS5hhE8U3Uzwn-E5127lQ')
