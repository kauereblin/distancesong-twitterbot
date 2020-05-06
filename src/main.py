#!/usr/bin/python
# -*- encoding: utf-8 -*-

import tweepy
# from time import sleep

from spot_api import query_music_duration
from route_timer import query_trip_duration

from config import *


""" def sleep_minutes(minutes):
    sleep(minutes * 60) """


def request_dms(bot):
    dms = bot.list_direct_messages()
    if dms:
        return dms
    else:
        return False


def get_text(dms):
    text = dms[0].message_create['message_data']['text']
    if text != '':
        return text, dms[0].id
    elif text == '':
        return False
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
    auth = tweepy.OAuthHandler(CONSUMER_KEY_TT, CONSUMER_SECRET_TT)
    auth.set_access_token(ACCESS_TOKEN_TT, ACCESS_TOKEN_SECRET_TT)
    api_bot = tweepy.API(auth)

    dms = request_dms(api_bot)

    if dms:
        _text = get_text(dms)[0]
        dm_id = get_text(dms)[1]
    else:
        raise Exception('Invalid Direct Message')

    data_list = get_msg_data(_text)

    items = set_items(data_list)

    update(items, api_bot, dm_id)


def update(items, bot, dm_id):
    music_duration = query_music_duration(items[0], items[1])
    trip_duration = query_trip_duration(items[2], items[3])

    bot.update_profile(name=f'Ouvindo {items[1]} de {items[0]}')

    message = set_message(music_duration, trip_duration,
                          items[1], items[2], items[3])
    bot.update_status(status=message)

    bot.destroy_direct_message(dm_id)


if __name__ == "__main__":
    main()
