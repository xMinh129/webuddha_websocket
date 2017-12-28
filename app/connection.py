import asyncio
import websockets
import quotes

start_server = websockets.serve(quotes.generator, 'localhost', 9677)

print('Webuddha is running on localhost')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
