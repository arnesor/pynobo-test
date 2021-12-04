import asyncio
from pynobo import nobo

async def main():
    # Either call using the three last digits in the hub serial
    hub = nobo('237', loop=asyncio.get_event_loop())
    # or full serial and IP if you do not want to discover on UDP:
#    hub = nobo('123123123123', '10.0.0.128', False, loop=asyncio.get_event_loop())

    # Connect to the hub
    await hub.start()

    # Inspect what you get
    def update(hub):
        print(hub.hub_info)
        print(hub.zones)
        print(hub.components)
        print(hub.week_profiles)
        print(hub.overrides)
        print(hub.temperatures)

    # Listen for data updates - register before getting initial data to avoid race condition
    hub.register_callback(callback=update)

    # Get initial data
    update(hub)

    # Hang around and wait for data updates
    await asyncio.sleep(60)

    # Stop the connection
    await hub.stop()


if __name__ == "__main__":
    asyncio.run(main())
