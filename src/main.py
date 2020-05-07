#!/usr/bin/python
# -*- encoding: utf-8 -*-

import tweepy
from time import sleep

from spot_api import query_music_duration
from route_timer import query_trip_duration

from config import *


def sleep_minutes(minutes):
    sleep(minutes * 60)


def auth_tweepy_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY_TT, CONSUMER_SECRET_TT)
    auth.set_access_token(ACCESS_TOKEN_TT, ACCESS_TOKEN_SECRET_TT)
    api_bot = tweepy.API(auth, wait_on_rate_limit=True)

    return api_bot


def request_dms(bot):
    dms = bot.list_direct_messages()
    if dms:
        return dms
    else:
        return False


def get_dm_text(dms):
    text = dms[0].message_create['message_data']['text']
    if text != '':
        return text, dms[0].id
    elif text == '':
        return False, dms[0].id
    else:
        raise Exception('Invalid text type')


def get_msg_data(_text):
    data_list = []
    text = _text.split('\n')
    for i in range(len(text)):
        data_list.extend(text[i].split(': '))

    data_list[:] = [data_list[i] for i in range(len(data_list))
                    if not data_list[i].lower() in
                    ['artista', 'música', 'musica', 'origem', 'destino']]

    return data_list


def set_items(data_list):
    artist = data_list[0].strip()
    music = data_list[1].strip()
    origin = data_list[2].replace(' ', '')
    destiny = data_list[3].replace(' ', '')

    return [artist, music, origin, destiny]


def set_message(msc_drt, trip_drt, music, origin, destiny):
    message = f'Você consegue ouvir {music} {trip_drt // msc_drt} \
vezes na viagem de {origin} para {destiny}!'

    return message


def main():
    api_bot = auth_tweepy_api()

    while True:
        dms = request_dms(api_bot)

        if dms:
            _text, dm_id = get_dm_text(dms)

            if _text:
                data_list = get_msg_data(_text)
            else:
                api_bot.send_direct_message(dm_id, ERROR_SPOT)

            items = set_items(data_list)

            update(items, api_bot, dm_id)
            sleep_minutes(1)
        else:
            sleep_minutes(5)
            api_bot.update_status('Será que alguém gosta de mim?')


def update(items, bot, dm_id):
    music_duration, music = query_music_duration(items[0], items[1])
    trip_duration = query_trip_duration(items[2], items[3])

    if trip_duration:
        bot.update_profile(name=f'Ouvindo {music} de {items[0]}',
                           location=f'Indo para {items[3]}')

        message = set_message(music_duration, trip_duration,
                              music, items[2], items[3])
        bot.update_status(status=message)

        bot.destroy_direct_message(dm_id)

    else:
        bot.send_direct_message(dm_id, ERROR_MAP)


if __name__ == "__main__":
    main()
