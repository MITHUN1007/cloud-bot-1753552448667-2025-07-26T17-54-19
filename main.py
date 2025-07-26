from telethon import TelegramClient, events

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(pattern='(?i)gro'))
async def echo(event):
    await event.reply('You mentioned gro!')

client.start()
client.run_until_disconnected()