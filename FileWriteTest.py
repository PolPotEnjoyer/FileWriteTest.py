import os


def displayContents():
    a = open("file1.txt", "r")
    print(a.read())
    print("[End of file]")
    a.close()
    menu()

def writeToFile():
    writing = "y"
    while writing == "y":
        a = open("file1.txt", "a")
        def newline():
            newLine = input("New Line (y/n)?" )
            newLine = newLine.lower()
            if newLine == "y":
                a.write("\n")
            elif newLine != "y" and newLine != "n":
                print("invalid input")
                newline()
        newline()
        textEntry = input("Input the text you want to add: ")
        a.write(textEntry)
        a.close()
        print("File now reads:")
        a = open("file1.txt", "r")
        print(a.read())
        print("[End of file]")
        print()
        writing = input("continue writing (y/n)? ")
        writing = writing.lower()
    a.close()
    menu()

def purge():
    choice = input("are you sure (y/n)? ")
    choice = choice.lower()
    if choice == "y":
        os.remove("file1.txt")
        print("File deleted")
        menu()
    elif choice == "n":
        menu()



def menu():
    for x in range(3):
        print()
    print("Welcome to the file modifier")
    print()
    def selector():
        print("r to read, w to write, p to purge")
        select = input()
        select = select.lower()
        if select == "r":
            displayContents()
        elif select == "w":
            writeToFile()
        elif select == "p":
            purge()
        else:
            print("invalid input")
            selector()
    selector()


menu()
