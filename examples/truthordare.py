import dhravyapy
import asyncio

async def main():
    # Assign a variable for the truth or dare
    tod = dhravyapy.Fun.truthordare()
    # Takes the truth property of the tod variable
    truth = tod.truth
    # Takes the dare property of the tod variable
    dare = tod.dare
    # Prints the dare
    print(f"If you want dare... here is a dare : {dare}")
    # Prints the truth
    print(f"If you want a truth... here is a truth : {truth}")

if __name__ == __main__:
    # Creates and runs the async loop synchronously
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
