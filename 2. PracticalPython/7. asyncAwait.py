# Asynchronous programming allows the program to work on other tasks while waiting for an operation, such as a network request, to complete.

# Normal function

import time

def download_file():
    print("Downloading..")
    time.sleep(2)
    print("Download Completed")

download_file()
print("----------")

# time.sleep(2) blocks the current thread for two seconds.

# --------------------------------------------------

# async and await function

import asyncio

async def download_File():
    print("Download Started..")
    await asyncio.sleep(2)
    print("Download Completed")

asyncio.run(download_File())
print("----------")

# What changed?

    # async def defines a coroutine function.
    # await pauses that coroutine while an awaited operation is incomplete, allowing the event loop to run other work.
    # asyncio.sleep(2) waits without blocking the event loop.
    # asyncio.run() starts and manages the event loop for this simple program.

# ---------------------------------------------------------

# Run multiple tasks concurrently

async def fetch_data(name, delay):
    print(f"Starting {name}")

    await asyncio.sleep(delay)

    print(f"Finished {name}")
    return f"{name} data"

async def main():
    results = await asyncio.gather(
        fetch_data("API_1", 2),
        fetch_data("API_2", 2),
        fetch_data("API_3", 2)
    )
    print(results)

asyncio.run(main())
