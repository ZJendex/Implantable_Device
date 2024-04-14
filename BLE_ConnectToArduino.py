import asyncio
from bleak import BleakClient

address = "04A6A1DF-986C-785B-6EE7-6DDC2E7685CC"  # Get from BLE_DiscoverDevice.py
UUID_CHARACTERISTIC = "19B10011-E8F2-537E-4F6C-D104768A1214"  # The UUID of the characteristic from arduino code init

async def connect_and_read(address):
    async with BleakClient(address) as client:
        connected = await client.is_connected()
        print(f"Connected: {connected}")

        # Read the characteristic
        value = await client.read_gatt_char(UUID_CHARACTERISTIC)
        print(f"Characteristic value: {value}")

loop = asyncio.get_event_loop()
loop.run_until_complete(connect_and_read(address))
