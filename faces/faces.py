def convert():
    emoji = input("Please show us your emotions with emoji - :)  or  :(  """).replace(":)","🙂").replace(":(","🙁")                                      
    return emoji

def main():
    print(convert())
     


main()


