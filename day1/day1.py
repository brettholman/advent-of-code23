from re import sub, compile

lookup = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine",
    "[a-z]": ""
}


def replace_all_in_file(file, str, replace):
    regex = compile(r"{}".format(str))
    return sub(regex, replace, file)


def sanitize_file(file):
    for w, r in lookup.items():
        file = replace_all_in_file(file, w, r)
    return file


def main():
    file_handler = open("./input.txt", "r")
    file = file_handler.read()
    lines = sanitize_file(file).split("\n")
    total = 0
    new_line_regex = compile(r"/\n")
    for line in lines:
        line = sub(new_line_regex, "", line)
        if len(line) == 0:
            break
        num = int("{}{}".format(line[0], line[-1]))
        total += num
    print(total)


if __name__ == '__main__':
    main()
