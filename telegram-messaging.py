# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 'Enter apiId'
api_hash = 'Enter apiHash'
token = 'Enter TOKEN'

# your phone number
phone = 'Enter phone number associated with telegram'

client = TelegramClient('session', api_id, api_hash)
# connecting and building the session
client.connect()
if not client.is_user_authorized():
	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code camed on telegram: '))

messageTobeSent = "WORKING... message sent by bot"
username = "@samyak1409" #username whom message to be sent

try:
	user = client.get_input_entity(username)
	print(user)
	receiver = InputPeerUser(user.user_id, user.access_hash)
	client.send_message(receiver, message, parse_mode='html')
except Exception as e:
	# there may be many error coming in while like peer
	# error, wrong access_hash, flood_error, etc
	print(e);
client.disconnect()
