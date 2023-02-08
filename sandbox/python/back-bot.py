import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6010132260:AAHCUMUAvpz_bsaQKavFa1vIzVa5izMw_CU'
TEXT: str = 'Ура! Классный апдейт!'
TEXT202: str = 'кто-то прислал посыл)'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

chat_id202: int
text_message: str
chat_username: str
txt_202: str

print('start after night')
updatesNight = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates').json()
if updatesNight['result']:
    for result in updatesNight['result']:
        # offset = result['update_id']
        chat_id = result['message']['from']['id']
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

        chat_id202 = 394257307
        # chat_username = result['message']['chat']['username']
        chat_username = result['message']['chat']['last_name']
        text_message = result['message']['text']
        # txt_202 = TEXT202
        txt_202 = 'username: ' + chat_username + ' message: ' + text_message
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id202}&text={txt_202}')


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

            chat_id202 = 394257307
            # chat_username = result['message']['chat']['username']
            chat_username = result['message']['chat']['last_name']
            text_message = result['message']['text']
            # txt_202 = TEXT202
            txt_202 = 'username: ' + chat_username + ' message: ' + text_message
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id202}&text={txt_202}')

    time.sleep(1)
    counter += 1