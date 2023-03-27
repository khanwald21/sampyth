
'''
-> This program enables user to login to Telegram Client account
-> Client listens oncoming notifications from the terminal

'''

#libraries 
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.types import PeerChannel

#user info 
username = input('Enter your telegram alias ')
api_id = input('Enter your api id')
api_hash = input('Enter your api hash')
chats = input('Enter Groups to listen')

#create a telegram client
try:
  client = TelegramClient(username, api_id, api_hash)
  client.start()
  print('  CLIENT SUCCESFUL  ')
  @client.on(events.NewMessage(chats = chats))
  async def newMessageListener(event):
    newMessage = event.message.message
    await client.forward_messages(entity='me', messages = event.message)
    print(newMessage) 
  with client:
    client.run_until_disconnected()
except:
  print('  ERROR : CLIENT UNSUCCESSFUL  ')
  