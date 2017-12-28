import random
import io
import os
import json
import secrets
import asyncio

current_dir = os.path.dirname(os.path.realpath(__file__))
with io.open(os.path.join(current_dir, 'quotes.json'), 'rb') as quotes_file:
    quotes_as_string = quotes_file.read()

quotes = json.loads(quotes_as_string)

async def generator(websocket, path):
    random_quote = secrets.choice(quotes)
    print(random_quote)
    await websocket.send(random_quote['quoteText'])
    await asyncio.sleep(3)
