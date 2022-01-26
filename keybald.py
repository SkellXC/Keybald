keybinded = input("Is keybinded bald? \n ")
if keybinded.lower() in ["yes", "yea", "duh", "yep"]:
    print("True!")
    baldscale = int(input("Enter a scale of how bald keybinded is \n"))
    if baldscale >= 10:
        print("Correct. They wild keybald is usually 110-115% bald!")
    else:
        print("Cap. Opinion = invalid")
                    
elif keybinded.lower() in ["no", "nah", "cap"]:
    print("Shut up loser")
    exit()
      
else:
     print("Invalid input, fyi, he is bald.")
