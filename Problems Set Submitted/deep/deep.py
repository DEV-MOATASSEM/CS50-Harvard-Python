xy=input("What is the answer to the Great Question of Life, the Universe and Everything?").casefold()

xy=xy.strip()

match xy:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")