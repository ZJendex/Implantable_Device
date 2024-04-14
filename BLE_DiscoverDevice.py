import asyncio
from bleak import BleakScanner

async def discover():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device {device.name}: {device.address}")

loop = asyncio.get_event_loop()
loop.run_until_complete(discover())
