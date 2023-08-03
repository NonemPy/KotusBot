import disnake
from disnake.ext import commands
import time
import aiofiles
from enum import Enum
import random
from disnake.enums import ButtonStyle
import asyncio

#   EDITABLE THINGS ↓

bottoken = "тут токен"

defaultembedcolor = disnake.Colour.green()

defaulterrorembedcolor = disnake.Colour.red()

#   EDITABLE THINGS ↑



intents = disnake.Intents.all()

Bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned,
    intents=intents,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="Alexsovi by NonemPy#0001")
)


Bot.warnings = {}

hug_gifs = [
    'https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif',
    'https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif'
]

kiss_gifs = [
    'https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif'
]

roles = {
    "Red": "1052714857113325589",
    "Orange": "1052714932761808949",
    "Yellow": "1052715015062442137",
    "Blue": "1052715229475246110"
}

@Bot.slash_command(name="role", description="Выбрать роль")
async def role(ctx, role_name: str):
    member = ctx.author
    guild = ctx.guild

    role_id = roles.get(role_name)

    if role_id:
        role = disnake.utils.get(guild.roles, id=int(role_id))

        if role:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f"Роль {role.name} успешно удалена.")
            else:
                await member.add_roles(role)
                await ctx.send(f"Роль {role.name} успешно добавлена.")
        else:
            await ctx.send("Неверный ID роли.")
    else:
        await ctx.send("Неверное имя роли.")



@Bot.slash_command()
async def разраб(interaction: disnake.AppCmdInter):
    await interaction.send("вы получите  значок   разраба через 24 часа ")

log_channel_id = 1052515982847004723  # Замените на идентификатор вашего канала для логов


@Bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel:
            await log_channel.send(f"{member.name} зашел в голосовой канал {after.channel.name}.")
        else:
            await log_channel.send(f"{member.name} вышел из голосового канала {before.channel.name}.")

@Bot.event
async def on_message_edit(before, after):
    await log_channel.send(f"Сообщение {before.author.name} изменилось: `{before.content}` -> `{after.content}`")

@Bot.event
async def on_message_delete(message):
    await log_channel.send(f"Сообщение {message.author.name} было удалено: `{message.content}`")

@Bot.event
async def on_member_join(member):
    await log_channel.send(f"{member.name} присоединился к серверу.")

@Bot.event
async def on_member_remove(member):
    await log_channel.send(f"{member.name} покинул сервер.")

@Bot.event
async def on_member_ban(guild, user):
    await log_channel.send(f"{user.name} был забанен на сервере {guild.name}.")

@Bot.event
async def on_member_unban(guild, user):
    await log_channel.send(f"{user.name} был разбанен на сервере {guild.name}.")




@Bot.event
async def on_ready():
    
    for guild in Bot.guilds:
        Bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"warnings/{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"warnings/{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                pointintime = int(data[2])
                reason = " ".join(data[3:]).strip("\n")

                try:
                    Bot.warnings[guild.id][member_id][0] += 1
                    Bot.warnings[guild.id][member_id][1].append((admin_id, pointintime, reason))

                except KeyError:
                    Bot.warnings[guild.id][member_id] = [1, [(admin_id, pointintime, reason)]] 
    
    
    print(f'Logged in as "{Bot.user}" ✔')

@Bot.slash_command()
async def kiss(self, inter, member:disnake.Member):
        gifs = [
            "https://tenor.com/ru/view/kiss-gif-22640695",
            "https://tenor.com/ru/view/kiss-hug-heart-love-gif-26161529",
            "https://tenor.com/ru/view/kiss-love-good-morning-gif-23457871"
        ]
        gif = random.choice(gifs)
        embed = disnake.Embed(title="Kiss", description=f"{ctx.author.mention} kisses someone!", color=discord.Color.blurple())
        embed.set_image(url=gif)

@Bot.slash_command(name="clear", usage=f"clear [amount]")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    emb = disnake.Embed(
    description=f"{ctx.author.mention} очистил {amount} сообщений")
    await ctx.send(embed=emb)

@Bot.slash_command()
async def hug(self, inter, member:disnake.Member):
        gifs = [
            "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif",
            "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif"
        ]
        gif = random.choice(gifs)
        embed = disnake.Embed(title="Hug", description=f"{ctx.author.mention} gives someone a hug!", color=discord.Color.blurple())
        embed.set_image(url=gif)

@Bot.slash_command(name = 'shar', description = 'Отвечает на вопрос участника.', usage = 'шар Вопрос')
async def шар(self, inter, *, question):
        responses = [
            'Это точно 👌',
            'Очень даже вряд-ли 🤨',
            'Нет ❌',
            'Да, безусловно ✔',
            'Вы можете рассчитывать на это 👌',
            'Вероятно 🤨',
            'Перспектива хорошая 🤔',
            'Да ✔',
            'Знаки указывают да 👍',
            'Ответ туманный, попробуйте еще раз 👀',
            'Спроси позже 👀',
            'Лучше не говорить тебе сейчас 🥵',
            'Не могу предсказать сейчас 👾',
            'Сконцентрируйтесь и спросите снова 🤨',
            'Не рассчитывай на это 🙉',
            'Мой ответ - Нет 😕',
            'Мои источники говорят нет 🤨',
            'Перспективы не очень 🕵️‍♂️',
            'Очень сомнительно 🤔'
        ]
        embed = disnake.Embed(
            description=f'🎱 8ball', 
            timestamp=inter.created_at
        )
        embed.add_field(name=f'**Вопрос от {inter.author}:**', value=question, inline=True)
        embed.add_field(name='**Ответ: **', value=random.choice(responses), inline=False)
        embed.set_thumbnail(url=inter.author.display_avatar.url)
        await inter.response.send_message(embed=embed)

    
@Bot.event
async def on_guild_join(guild):
    Bot.warnings[guild.id] = {}(nult_member_permissions=disnake.Permissions(moderate_members=True))
async def moderation(inter):
    pass

    name='ban',
    description='Забанить пользователя'

async def slash_ban(ctx, user: disnake.User, reason: str = None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send('У вас нет прав на использование этой команды.')
        return

    if reason is None:
        reason = 'Не указана'

    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f'Пользователь {user.mention} был забанен. Причина: {reason}.')

@Bot.slash_command(
    name='kick',
    description='Выгнать пользователя'
)
async def slash_kick(ctx, user: disnake.Member, reason: str = None):
    if not ctx.author.guild_permissions.kick_members:
        await ctx.send('У вас нет прав на использование этой команды.')
        return

    if reason is None:
        reason = 'Не указана'

    await user.kick(reason=reason)
    await ctx.send(f'Пользователь {user.mention} был выгнан. Причина: {reason}.')

@Bot.slash_command(
    name='mute',
    description='Выдать мут пользователю'
)
async def slash_mute(ctx, user: disnake.Member, duration: int = None, reason: str = None):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send('У вас нет прав на использование этой команды.')
        return

    role = disnake.utils.get(ctx.guild.roles, name='Muted')
    if role is None:
        await ctx.send('Роль Muted не найдена на сервере.')
        return

    if duration is None:
        duration = 0

    if reason is None:
        reason = 'Не указана'

    await user.add_roles(role, reason=reason)
    await ctx.send(f'Пользователь {user.mention} получил мут на {duration} минут(ы). Причина: {reason}.')



@Bot.slash_command(
    name='warn',
    description='Выдать предупреждение пользователю'
)
async def slash_warn(ctx):
    # Реализуйте логику команды warn
    pass

@Bot.slash_command(
    name='delete_warn',
    description='Удалить предупреждение у пользователя'
)
async def slash_delete_warn(ctx):
    # Реализуйте логику команды delete_warn
    pass


@Bot.event
async def on_member_update(before, after):
    guild = after.guild
    channel_id = 1052515982847004723  # Замените на ID канала, в который нужно отправлять журнал аудита

    if after.guild != guild:
        return

    if before.display_name != after.display_name:
        channel = bot.get_channel(channel_id)
        await channel.send(f'Member {after.mention} changed their nickname: {before.display_name} -> {after.display_name}')

@Bot.event
async def on_message_delete(message):
    guild = message.guild
    channel_id = 1052515982847004723  # Замените на ID канала, в который нужно отправлять журнал аудита

    if message.guild != guild:
        return

    channel = Bot.get_channel(channel_id)
    await channel.send(f'удаленно сообщение #{message.channel.name}: {message.author.mention}: {message.content}')

@Bot.event
async def on_message_edit(before, after):
    guild = before.guild
    channel_id = 1052515982847004723  # Замените на ID канала, в который нужно отправлять журнал аудита

    if before.guild != guild:
        return

    channel = Bot.get_channel(channel_id)
    await channel.send(f'Сообщение #{before.channel.name} было изменено: {before.author.mention}\n'
                       f'Старое содержимое: `{before.content}`\n'
                       f'Новое содержимое: `{after.content}`')





@Bot.slash_command(
    name="say",
    description="Отправить сообщение от имени бота."
)
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, message):
    await ctx.send(message)
        
@Bot.slash_command(name="rules1", description="Help for commands")
async def help(inter):
    embed = disnake.Embed (
        title="RULES",
        description=f'правила нашего сервера',
        colour = defaultembedcolor
    )
    
    embed.add_field(name="1.1", value="флуд", inline=False)
    embed.add_field(name="1.2", value="оффтоп", inline=False)
    embed.add_field(name="1.3", value="Неадекватное поведение, разжигание срачей в чате", inline=False)
    embed.add_field(name="2.1", value="Оскорбления родных в любом виде", inline=False)
    embed.add_field(name="2.2", value="Немецкая свастика в любом виде", inline=False)
    embed.add_field(name="2.3", value="Публикация nsfw контента, шок контента, а также контента способного навредить психике человека", inline=False)
    embed.add_field(name="2.4", value="реклама",inline=False)
    embed.add_field(name="2.5", value="Слив личной информации участников без из согласия ( дианоны )",inline=False)
      
        

        
    
    
@Bot.slash_command(default_member_permissions=disnake.Permissions(moderate_members=True))
async def user(inter):
    pass
@user.sub_command(name="info", description="See information about a member")
async def info(inter, member:disnake.Member):
    
    for guild in Bot.guilds:
        Bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"warnings/{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"warnings/{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                pointintime = int(data[2])
                reason = " ".join(data[3:]).strip("\n")

                try:
                    Bot.warnings[guild.id][member_id][0] += 1
                    Bot.warnings[guild.id][member_id][1].append((admin_id, pointintime, reason))

                except KeyError:
                    Bot.warnings[guild.id][member_id] = [1, [(admin_id, pointintime, reason)]] 
    
    
    date_time = str(member.created_at)
    
    cut_date_time = date_time[0:19]
    
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(cut_date_time, pattern)))
    
    try:
        count = Bot.warnings[inter.guild.id][member.id][0]
    except KeyError:
        count = "0"
    
    embed = disnake.Embed(
        title="User Info",
        color=defaultembedcolor
    )
    
    embed.set_author(
        name=str(member.name+"#"+member.discriminator),
    )
    
    embed.set_thumbnail(
        url=member.avatar.url if member.avatar else disnake.Embed.Empty 
    )
    
    embed.add_field(name="Username", value=str('`'+member.name+"#"+member.discriminator+'`'), inline=True)
    embed.add_field(name="Nickname", value=str('`'+member.display_name+'`'), inline=True)
    embed.add_field(name="User ID", value=str('`'+str(member.id)+'`'), inline=False)
    embed.add_field(name="Is bot?", value=str('`'+str(member.bot)+'`'), inline=True)
    embed.add_field(name="Created at", value=f"<t:{str(epoch)}:f>", inline=False)
    embed.add_field(name="Warnings", value='`'+str(count)+'`', inline=False)
    
    await inter.send(embed=embed)
    
    
    
@Bot.slash_command(name="help", description="Help for moderation commands")
async def help(inter):
    
    embed = disnake.Embed (
        title="FQQDs Moderation Bot - Moderation Help",
        description=f'Here you can find some help for every moderation command.\nMembers are notified per direct message for every action\nFor every moderation command the "Moderate Members" permission is required',
        colour = defaultembedcolor
    )
    
    embed.add_field(name="/moderation ban", value="Ban members (Use Discord intern feature for message removal)", inline=False)
    embed.add_field(name="/moderation kick", value="Kick members", inline=False)
    embed.add_field(name="/moderation warn", value="Warn members", inline=False)
    embed.add_field(name="/moderation warnings", value="See all warnings of a member", inline=False)
    embed.add_field(name="/moderation removewarnings", value="Remove warnings of a member", inline=False)
    embed.add_field(name="/user info", value="See information about a member", inline=False)
    
    
    await inter.send(embed=embed)

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        # Обработка ошибки при выполнении команды
        await ctx.send("Произошла ошибка при выполнении команды.")
    elif isinstance(error, commands.CommandNotFound):
        # Обработка ошибки "команда не найдена"
        await ctx.send("Указанная команда не существует.")
    # Добавьте другие обработчики ошибок по необходимости

    

@commands.Cog.listener()
async def on_command_error(self, inter, error):
        print(error)

        if isinstance(error, commands.MissingPermissions):
            embed = disnake.Embed( title = 'Ошибка!', description = f'{inter.author.mention}, у вас нет прав на выполнения этой команды!', colour = botmaincolor)
            embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
            await inter.send(embed = embed)

        if isinstance(error, commands.CommandNotFound):
            embed = disnake.Embed(title = 'Ошибка!', description = f'{inter.author.mention}, данной команды не существует! Посмотри список доступных команд по команде **`{PREFIX}хелп`**!', colour = botmaincolor)
            embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
            await inter.send(embed = embed)

        if isinstance(error, commands.CommandOnCooldown):
            hour = round(error.retry_after/3600)
            minute = round(error.retry_after/60)

            if hour > 0:
                embed = disnake.Embed( title = 'Эээммм полегче!', description = f'**Воууу, полегче {inter.author.mention}!** Похоже, что ты нарушаешь **кулдаун команд!**\nПовтори через `{str(hour)}` час(ов/а)', colour = botmaincolor)
                embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
                await inter.send(embed = embed)
            elif minute > 0:
                embed = disnake.Embed( title = 'Эээммм полегче!', description = f'**Воууу, полегче {inter.author.mention}!** Похоже, что ты нарушаешь **кулдаун команд!**\nПовтори через `{str(minute)}` минут(ы)', colour = botmaincolor)
                embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
                await inter.send(embed = embed)
            else:
                embed = disnake.Embed(title = 'Эээммм полегче!', description = f'**Воууу, полегче {inter.author.mention}!** Похоже, что ты нарушаешь **кулдаун команд!**\nПовтори через `{error.retry_after :.0f}` секунд(ы)', colour = botmaincolor)
                embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
                await inter.send(embed = embed)

        if isinstance(error, commands.errors.MemberNotFound):
            embed = disnake.Embed(description = f'{inter.author.mention}, указанный пользователь не найден.', colour = botmaincolor)
            embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
            await inter.send(embed = embed)

        if isinstance(error, commands.UserInputError):
            embed = disnake.Embed(title = 'Ошибка!', description=f'**Правильное использование команды:** `{PREFIX}{inter.command.name}`\n**Example:** `{PREFIX}{inter.command.usage}`', colour = botmaincolor)
            embed.set_footer(text = f'{footerbyriverya4life}', icon_url =avatarbyfooterbyriverya4life)
            await inter.send(embed = embed)
    
@Bot.slash_command(name="credit", description="Credits of the bot")
async def credit(inter):
    embed = disnake.Embed (
        title="FQQDs Moderation Bot - Credits",
        description=f'Bot coded by FQQD#2557\nGithub: https://github.com/FQQD/simple-moderation-bot/\nhttps://www.FQQD.de',
        colour = defaultembedcolor
    )  
    await inter.send(embed=embed) 
    
    
@Bot.slash_command(name="avatar", description="Show and download the profile picture of a user")
async def avatar(inter, member:disnake.Member):
    embed = disnake.Embed(
        title=f"Avatar of {member.name}#{member.discriminator}",
        description=f"URL: {member.avatar.url}",
        color=defaultembedcolor,
    )
    embed.set_image(
    url=member.avatar.url,
    )
    
    embed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar))
    embed.set_footer(text=f"Requested by {inter.author.name}", icon_url = '{}'.format(inter.author.avatar))
    
    
    await inter.send(embed=embed)



Bot.run(bottoken)

