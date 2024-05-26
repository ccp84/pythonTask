
def read_file():

    message = []

    with open("code.txt") as secret:
        for line in secret:
            newline = line.strip('\n')
            message.append(newline)
            message = sorted(message)

    return message


def print_message(message):

    decoded = ""

    i = 1
    j = 1
    while j <= len(message):

        block = message[:j]
        add = block.pop()
        add = add.split(' ')
        add = add.pop()
        decoded = decoded + " " + add
        i += 1
        j = j + i

    print(decoded)


def main():
    message = read_file()
    print_message(message)


main()
