from re import findall, compile

max_red = 12
max_green = 13
max_blue = 14

lookup = {
    12: r"(\d+) (red)",
    13: r"(\d+) (green)",
    14: r"(\d+) (blue)"
}


def part1():
    cur_line = 1
    total = 0
    file_handler = open("./input.txt", "r")
    for line in file_handler.readlines():
        game = line.split(":")[1]
        success = True
        for lookup_val in lookup.keys():
            val = max(
                list(
                    map(
                        lambda key: int(key[0]),
                        findall(compile(lookup[lookup_val]), game)
                    )
                )
            )
            if lookup_val < val:
                success = False
        if success:
            total += cur_line
        cur_line += 1

    print(total)


def part2():
    power_total = 0
    file_handler = open("./input.txt", "r")
    for line in file_handler.readlines():
        total = 1
        game = line.split(":")[1]
        for lookup_val in lookup.keys():
            val = max(
                    list(
                        map(
                            lambda val: int(val[0]),
                            findall(compile(lookup[lookup_val]), game)
                        )
                    )
            )
            total *= val
        power_total += total
    print(power_total)


if __name__ == "__main__":
    print("PART ONE")
    part1()
    print("PART TWO")
    part2()
