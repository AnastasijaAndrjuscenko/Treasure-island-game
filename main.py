from art import *

print(logo, intro)
left_right_lower = (input("You are on the crossroad, where do you want to go? Left or Right?")).lower()

if left_right_lower == "left":
    swim_wait = (input(
        "Mission continues...\nYou are next to the dark and huge lake and... Do you hear it...? Something is moving in "
        "the bushes and screaming. You should react immediately.\nWhat do you want to do? Swim or wait?")).lower()

    if swim_wait == "wait":
        door = (input(
            "The danger is over, but you fall asleep and forgot where is the exit.\nIn front of you are three doors. "
            "Red door in the dark forest. Blue door in the sand full of scorpions. Yellow door full of wild and "
            "hungry tigers. \nWhich color of the door you choose?")).lower()
        if door == "red":
            print(f"Burned by fire.\nGAME OVER!\n{fire}")
        elif door == "blue":
            print(f"You are eaten by beasts.\nGAME OVER!\n{beast}")
        elif door == "yellow":
            print(f"You are lucky. You Win!\n{bills}")
        else:
            print(f"You were eaten by hungry student.\nGAME OVER!\n{hungry}")
    else:
        print(f"You were attacked by trout.\nGAME OVER!\n{trout}")
else:
    print(f"You failed into a hole.\nGame over!\n{hole}")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
