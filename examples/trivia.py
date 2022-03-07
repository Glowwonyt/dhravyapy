import dhravyapy
import asyncio
# -------------- Imports --------------------------- #


async def main():
    trivia = dhravyapy.Info().trivia()
    question = trivia.question
    ans = trivia.answer
    
    # Just created the question and answer variable

    x = input(f"{question} \n Type the answer...")
    # Asks them to  to input an answer
    if x.lower() == ans.lower():
        #checks if the results match
        print("Good job you got the right answer")
    else:
        #compliments for the hard work
        print(":/ Lets do a different answer next time")


if __name__ == __main__:
    # Creates and runs an the async loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
