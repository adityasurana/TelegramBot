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

chats = []
last_date = None
chunk_size = 200
groupsList = []

# establishing request

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash = 0
))
chats.extend(result.chats)

# getting all chats and making cluster of groups separate in groupsList
for chat in chats:
    try:
        if chat.megagroup == True:
            groupsList.append(chat)
    except:
        continue

print('Choose a group to add members:')
i=0
# printing groupsList
for group in groupsList:
    print(str(i) + '- ' + group.title)
    i+=1
target_group = groups[1] # to groups in which user to be find
print(target_group)

all_participants = []
all_participants = client.get_participants(target_group, aggressive=True) # getting all users from group
for user in all_participants:
    if user.username:
        username= user.username
    else:
        username= ""
    if user.first_name:
        first_name= user.first_name
    else:
        first_name= ""
    if user.last_name:
        last_name= user.last_name
    else:
        last_name= ""
    name = (first_name + ' ' + last_name).strip()
    print(name)
    print(username)
    #user either of them name or username
# disconnecting the telegram session

client.disconnect()
