def convert(input):
    input=input.replace(":)","🙂")
    input=input.replace(":(","🙁")
    return input

def main():
    x=input(">>")
    print(convert(x))
main()