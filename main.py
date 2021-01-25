# This program is suppose to make writing github .readme files much more easier for me
# It's also suppose to be the first stages of, making a GUI based text editor
# These are all projects intended for myself.
# Still a work in progress, proably won't finish this project.

def menU():
    print ("""
1. Add Heading 2. Add paragraph 3. Add Code Block 4. Add Quote
5. Quit
""")

def writE():
    print("Enter file name. Don't add file extension. ")
    filename = input("> ")
    menU()
    while True: # This will loop the program
        options = input("> ")
        if options == '1':
            header = input("Give a header to write > ")
            with open(filename, 'a+') as f:
                f.write("\n# " + (header)) # # Gives (string) a header tag
                f.write("\n")
                f.close()
        elif options == '2':
            para = input("Type Paragraph: ")
            with open(filename, 'a+') as f:
                f.write("\n" + para)
                print(f.read())
                f.close()
        elif options == '3':
            codeblock = input("Input code: ")
            with open(filename, 'a+') as f:
                f.write("\n```python") # makes python as default programming language
                f.write("\n" + codeblock)
                f.write("\n```")
                f.close()
        elif options == '4':
            quote = input("Quote: ")
            with open(filename, 'a+') as f:
                f.write("\n> " + quote)
                f.close()
        elif options == '5':
            print("Goodbye...")
            break # Exit the loop

def main():
    print ("Would you like to edit a pre-existing file or create a new one?")
    print("1. Create")
    print("2. Edit")
    answer = input("[*]: ")
    if answer == '1':
        print("Give me a file name to create.")
        filename = input("> ")
        filename2 = (filename + ".md") # Gives the file the .md exntension
        with open(filename2, "w+") as f: # Creating file, given by user
            f.write("\n")
            f.close()
        writE()
    elif answer == '2':
       writE()

main()

