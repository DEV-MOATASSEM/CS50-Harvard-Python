def main():
    input_string=input("camelCase:")
    for c in input_string:
        if c.isupper():
            input_string=input_string.replace(c,change(c))

    print(input_string)


def change(input_replace):
    input_replace=input_replace.lower()
    input_replace="_"+input_replace
    return input_replace


if __name__ == "__main__":
    main()