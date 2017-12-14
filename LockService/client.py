from clientlibrary import clientLibrary
import sys

if (len(sys.argv) < 3):
    print("Server usage: python Server.py [IP] [PORT]")
    sys.exit(0)

if __name__ == "__main__":

    address = "{}:{}".format(sys.argv[1], int(sys.argv[2]))

    while True:
        actionNum = int(input(
            "---------------------------------------\n"
            "|Input nuber of what you want to do:  |\n"
            "|1. View the file list.               |\n"
            "|2. Read a File.                      |\n"
            "|3. Add a new file.                   |\n"
            "|4. Edit a file.                      |\n"
            "|5. Delete a file                     |\n"
            "|                                     |\n"
            "|0. Exit.                             |\n"
            "---------------------------------------\n"))

        if actionNum == 1:
            clientLibrary.fileLists(clientLibrary, address)

        elif actionNum == 2:
            fileToOpen = input("Input the complete filename you want to open: ")
            clientLibrary.readFile(clientLibrary, address, fileToOpen)

        elif actionNum == 3:
            fileToAdd = input("Input the complete filename you want to add: ")
            fileData = input("Input what you want to add to the {}: ".format(fileToAdd))
            clientLibrary.addFile(clientLibrary, address, fileToAdd, fileData)

        elif actionNum == 4:
            fileToEdit = input("Input the complete filename you want to edit: ")
            if clientLibrary.isFileExist(clientLibrary, address, fileToEdit) :
                fileData = input("Input the new data in {}: ".format(fileToEdit))
                clientLibrary.lockAddToQueue(clientLibrary, address, fileToEdit)
                clientLibrary.editFile(clientLibrary, address, fileToEdit, fileData)
                clientLibrary.lockDeleteFromQueue(clientLibrary, address, fileToEdit)
            else:
                print("File do not exist!")

        elif actionNum == 5:
            fileToDelete = input("Input the complete filename you want to delete: ")
            if clientLibrary.isFileExist(clientLibrary, address, fileToDelete):
                yn = input("Are you sure you want to delete {} ? (Y/N)".format(fileToDelete))
                if yn == "n" or yn == "N":
                    continue
                clientLibrary.lockAddToQueue(clientLibrary, address, fileToDelete)
                clientLibrary.deleteFile(clientLibrary, address, fileToDelete)
                clientLibrary.lockDeleteFromQueue(clientLibrary, address, fileToDelete)
            else:
                print("File do not exist!")


        elif actionNum == 0:
            break

        else:
            print("Wrong Input!")

        input("Press enter to continue")