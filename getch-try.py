import getch as g

##char = getch.getch()
##
##if (char):
##    print(char)


while True:
    c = g.getch()
##    c = int(getch.getch())
    if c == ord('k'):
        print("you typed k")
    elif c == ord('q'):
        print("you typed q and I'm quitting")
        break  # Exit the while loop
