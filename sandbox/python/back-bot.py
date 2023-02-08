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

API_CATS_URL: str = 'https://aws.random.cat/meow'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
cat_response: requests.Response
cat_link: str

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

            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1