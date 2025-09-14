import random
import time

print("You wake up in a haunted house! 👻")
print("There are doors on your left, on your right and in front.")

spooky_messages = [
    "\033[34mBoo! Did I scare you? :3\033[0m",
    "\033[34mUwu~ I'm a spooky ghost! nyaaaaaaa~ :3\033[0m",
    "\033[34mTeeheeeee~ ○( ＾皿＾)っ Hehehe… >:3\033[0m",
]

while True:
    choice = input("Which direction do you choose?").lower()
    outcome = random.choice(["trap", "treasure", "spookie :3"])

    if outcome == "trap":
        print(f"Ayee! You fell into a trap door by choosing {choice}! Try again~ 💀")
        break
    elif outcome == "treasure":
        print(f"Yaaay! You found a GeForce RTX 4090 Founders Edition by choosing {choice}! wp! 🎉🔥")
        break
    else:
        print(random.choice(spooky_messages))
        time.sleep(2)
        print("You survived for now... but try again~! 🔄️")
