import discord
from discord.ext import commands
import sqlite3

# Создаем подключение к базе данных SQLite
conn = sqlite3.connect('loginsandpasswords.db')
cursor = conn.cursor()

# Создаем таблицу для хранения данных
cursor.execute('''CREATE TABLE IF NOT EXISTS userdata
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   username TEXT,
                   login TEXT,
                   password TEXT)''')
print(cursor.fetchall())
# Инициализируем бота
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)



@bot.tree.command(name='record', description='черкани сюда свой логин и пароль, а то как лох дырявый ходишь.')
async def records(interaction: discord.Interaction, login: str or int, *, password: str or int):
    user_id = interaction.user.id
    username = interaction.user.name
    # Проверяем, есть ли уже данный логин в базе данных
    cursor.execute("SELECT * FROM userdata WHERE login=?", (login,))
    existing_user = cursor.fetchone()
    if existing_user:
        await interaction.response.send_message("Сэр, данный логин уже занят, пожалуйста, выберите другой.")
    else:
        # Добавляем новую запись в базу данных
        cursor.execute("INSERT INTO userdata (user_id, username, login, password) VALUES (?, ?, ?, ?)",
                       (user_id, username, login, password))
        await interaction.response.send_message("Ну все петушок, твои данные у меня")
        conn.commit()
        cursor.execute("SELECT * FROM userdata")
        result = cursor.fetchall()
        print(result)
        print(cursor.rowcount, "запись добавлена")
    

@bot.event
async def on_ready():
    await bot.tree.sync()

# Запускаем бота
bot.run('')

