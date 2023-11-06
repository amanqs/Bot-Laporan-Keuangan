"""
import gspread
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
#from aiogram.utils import executor

# Masukan Bot Token Kalian
# Masukan URL GoogleSpreadSheets 
bot_token = '6599729691:AAHnQAudNH19zxziLEm7r8zpMfDv74-aZ3c'
sheets_url = 'https://docs.google.com/spreadsheets/d/1EOYO5oH91YQUGXan2RRymDJNu8U19FQfIunjq825vmY/edit?usp=sharing'

# Ubah Menjadi Nama File Json Key Kalian
# Harus Satu Folder Dengan bot.py File .json nya
gsheets = gspread.service_account(filename='filenya.json')
open_sheets = gsheets.open_by_url(sheets_url)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Try logged in !')
bot = Bot(token=bot_token)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['help','start'])
async def cara_pengunaan(pesan: types.Message):
    await pesan.answer('''
    
    Selamat Datang Di Bot Laporan Pengeluaran Uang ^_^
    
    Contoh Pengunaan :
        
        /new kategori #harga item
        /new makanan #5.000 roti,minuman
        
    Perhatian :
        
        • Jangan menggunakan spasi dalam kategori,item maupun harga
        
        Contoh tidak pake spasi :
            
            /new makanan #5.000 roti,makanan
        
        Contoh menggunakan spasi :
            
            /new makanan #5.000 roti makanan
            
    Bisa menggunakan , - _ dan sebagaianya.
    
    ''')

@dp.message_handler(commands=['new'])
async def laporan_uang(pesan: types.Message):
    x = pesan.text.replace('/new','')
    name = pesan.from_user.first_name
    id_name = pesan.from_user.id
    xy = x.split('#')
    dt = datetime.now()
    tgln = dt.strftime("%Y-%m-%d/%H:%M:%S")
    inserts = open_sheets.sheet1
    try:
        all = str(tgln)+xy[0]+xy[1]+' '+name+' '+str(id_name)
        splits = all.split()
        ins = inserts.append_row(splits)
        await pesan.answer('Laporan Berhasil !')
    except:
        await pesan.answer('Laporan Gagal, Pastikan Cara Pengunaanya Benar !')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(dp.start_polling())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
        loop.run_until_complete(loop.shutdown_asyncgens())
"""


from datetime import datetime
from pyrogram import Client, filters
from creds import *
import gspread

# Masukkan informasi kredensial bot Anda di file creds.py
# Example: 
# api_id = 12345
# api_hash = "your_api_hash"
# bot_token = "your_bot_token"

# Ubah Menjadi Nama File Json Key Kalian
# Harus Satu Folder Dengan bot.py File .json nya
gsheets = gspread.service_account(filename='filenya.json')
sheets_url = 'https://docs.google.com/spreadsheets/d/1EOYO5oH91YQUGXan2RRymDJNu8U19FQfIunjq825vmY/edit?usp=sharing'
open_sheets = gsheets.open_by_url(sheets_url)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Try logged in !')

app = Client("my_bot", api_id=creds.api_id, api_hash=creds.api_hash, bot_token=creds.bot_token)

@app.on_message(filters.command(['help', 'start']))
async def cara_pengunaan(client, message):
    await message.reply_text('''
    
    Selamat Datang Di Bot Laporan Pengeluaran Uang ^_^
    
    Contoh Pengunaan :
        
        /new kategori #harga item
        /new makanan #5.000 roti,minuman
        
    Perhatian :
        
        • Jangan menggunakan spasi dalam kategori,item maupun harga
        
        Contoh tidak pake spasi :
            
            /new makanan #5.000 roti,makanan
        
        Contoh menggunakan spasi :
            
            /new makanan #5.000 roti makanan
            
    Bisa menggunakan , - _ dan sebagainya.
    
    ''')

@app.on_message(filters.command(['new']))
async def laporan_uang(client, message):
    x = message.text.replace('/new', '')
    name = message.from_user.first_name
    id_name = message.from_user.id
    xy = x.split('#')
    dt = datetime.now()
    tgln = dt.strftime("%Y-%m-%d/%H:%M:%S")
    inserts = open_sheets.sheet1
    try:
        all = str(tgln) + xy[0] + xy[1] + ' ' + name + ' ' + str(id_name)
        splits = all.split()
        ins = inserts.append_row(splits)
        await message.reply_text('Laporan Berhasil !')
    except:
        await message.reply_text('Laporan Gagal, Pastikan Cara Penggunaannya Benar !')

if __name__ == '__main__':
    app.run()
