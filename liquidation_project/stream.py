import asyncio
import json
import os

import django
from django.utils import timezone
from websockets import connect
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liquidation_project.settings')
django.setup()

websocket_url = "wss://fstream.binance.com/ws/!forceOrder@arr"

async def binance_liquidations():
    """
    Connects to the Binance WebSocket and processes liquidation messages.

    This function establishes a WebSocket connection to the Binance WebSocket URL,
    retrieves liquidation messages, and saves them to the database using the Liquidation model.

    The liquidation messages are parsed and transformed into a dictionary containing
    relevant information such as symbol, side, order type, quantity, price, etc.

    Note:
    - Make sure the Django project is set up correctly before running this function.
    - The Liquidation model must be imported from 'liquidation_app.models'.

    Returns:
    None
    """
    async for websocket in connect(websocket_url):
        try:
            while True:
                msg = await websocket.recv()
                print(msg)
                msg = json.loads(msg)['o']
                data = {
                    'symbol': msg['s'],
                    'side': msg['S'],
                    'order_type': msg['o'],  
                    'time_in_force': msg['f'],
                    'original_quantity': msg['q'],
                    'price': msg['p'],
                    'average_price': msg['ap'],
                    'order_status': msg['X'],
                    'order_last_filled_quantity': msg['l'],
                    'order_filled_accumulated_quantity': msg['z'],
                    'order_trade_time': timezone.now()
                }
                from liquidation_app.models import Liquidation
                liquidation = Liquidation(**data)
                await sync_to_async(liquidation.save)()
        except Exception as e:
            print(e)
            continue

asyncio.run(binance_liquidations())

