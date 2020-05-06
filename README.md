# Distance of Song - Twitter Bot

A Twitter Bot that calculate how many times a music can be played in determined
trip that's the user provide both by a direct message.

>This is a project made to test me. I had to do a different and new thing to me,
>to prove that's I can take it.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the
libraries on `requirements.txt` file.

```bash
python -m pip install -r requirements.txt
```

## Usage

This application uses three different API's (Tweepy, MapQuest, Spotipy),
so you have to get API Key's of all. With these, you alter the `config.py` file.

```python
CONSUMER_KEY_TT = 'YOUR_CONSUMER_KEY_OF_TWITTER'
CONSUMER_SECRET_TT = 'YOUR_CONSUMER_SECRET_KEY_OF_TWITTER'
ACCESS_TOKEN_TT = 'YOUR_TOKEN_OF_TWITTER'
ACCESS_TOKEN_SECRET_TT = 'YOUR_SECRET_TOKEN_OF_TWITTER'

CONSUMER_KEY_MQ = 'YOUR_CONSUMER_KEY_OF_MAP_QUEST'
CONSUMER_SECRET_MQ = 'YOUR_CONSUMER_SECRET_KEY_OF_MAPQUEST'

SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_KEY_OF_SPOTIPY'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET_KEY_OF_SPOTIPY'
```

Then you run the application:

```bash
python main.py
```

>Remember to get in "src" folder to run

### Follow it

* @distanceSongBot

## Contributing
Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)