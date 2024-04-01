import discord
import time
from discord.ext import commands
from coonfig import settings
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
words = ['зевс', 'тор', 'машина', 'слон', 'жираф', 'акула', 'стриптезёр', 'гей', 'верующий', 'динозавр', 
         'макароны', 'Павел Воля', 'Райан Гослинг', 'Дэдпул', 'Человек Паук', 'Филипп Киркоров', 'Хоббит', 
         'Бенджамин Франклин', 'Дональд Трамп', 'Владимир Путин', 'даун', 'аутист', 'шизофреник', 'качок', 
         'муха', 'спирт', 'член', 'БМВ', 'мерседес', 'банан', 'червь', 'глисты', 'Даша Корейка', 'киллер',
         'Наруто', 'Скрудж Макдак', 'генерал', 'Билли Херингтон', 'повар', 'мудрец', 'гадалка', 'цыган',
         'оракул', 'солдат', 'Халк', 'Шрэк', 'Осёл', 'Винни Пух', 'Сергей Бодров', 'бобр', 'пингвин', 'учитель',
         'каратист', 'Крош', 'Совунья', 'Пин', 'гадюка', 'кактус', 'пилот', 'Лунтик', 'Моргенштерн', 'Рапунцель',
         'насильник', 'хулиган', 'Чукча', 'альбинос', 'Бэтмэн', 'геймер', 'программист', 'лень', 'Адольф Гитлер',
         'феминистка', 'раб', 'дракон', 'гаргулия', 'Жюль Верн', 'слепой']
game_started = False
word = {}

@bot.tree.command(name='start', description='start the fukin game')
async def start(interaction: discord.Interaction):
    global word
    global game_started
    if not game_started:
        game_started = True
        word[interaction.guild_id] = random.choice(words)
        await interaction.response.send_message(f'Тебе выпало слово "{word}". Объясни остальным, что это за слово.', ephemeral=True)  
        await interaction.channel.send(f'<@{interaction.user.id}> начал игру обьясняющего')
    else:
        await interaction.response.send_message('Игра уже начата. Нельзя использовать команду /start до того, как игра будет закончена.', ephemeral=True)
@bot.tree.command(name='whoo', description='who is it???')
async def whooooo(msg):
    await msg.channel.send(f'<@{msg.user.id}> на данный момент обьясняющий.')

@bot.tree.command(name='rules', description='uznay pravila igri')
async def rul(msg):
    await msg.channel.send(f'Правила игры довольно просты! \n Бот задает обьясняющему слово, ваша задача отгдаь его по описанию обьясняющего.')    

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.tree.sync()

@bot.event
async def on_message(msg):
    if msg.author != bot.user:
        if msg.guild.id in word:
            if msg.content.lower() == word[msg.guild.id].lower():
                await msg.reply('Верно!')
                global game_started
                del word[msg.guild.id]
                game_started = False

bot.run(settings['token'])