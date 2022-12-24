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
	client.sign_in(phone, input('Enter the code: '))

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
target_group = groups[1] # to groups in which user to be added
print(target_group)

# username of user whome we want to add 
username = "@samyak1409"

# getting clients user_id and user_access_hash
user_to_add = client.get_input_entity(username)

target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

# adding user to group
try:
    client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    print("added successfully")