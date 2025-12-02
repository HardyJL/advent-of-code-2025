def part_two(input: list[str]) -> int:
    amount = 0
    total = len(input)
    for curr, line in enumerate(input):
        print(f"{curr} / {total}")
        lower, upper = line.split("-")
        for i in range(int(lower), int(upper) + 1):
            streval = str(i)
            for j in range(1, len(streval) // 2 + 1):
                split_list = {streval[x : x + j] for x in range(0, len(streval), j)}
                if len(split_list) <= 1:
                    amount += i
                    break

    return amount


def part_one(input: list[str]) -> int:
    amount = 0
    for line in input:
        lower, upper = line.split("-")
        # print(f"{lower} - {upper}")
        for i in range(int(lower), int(upper) + 1):
            streval = str(i)
            if len(streval) % 2 != 0:
                continue
            midway = len(streval) // 2
            left = streval[:midway]
            right = streval[midway:]
            if left == right:
                print(left, right)
                amount += i
    return amount


def main() -> None:
    line = ""
    with open("day2/day2.txt") as file:
        line = file.readline()
    lines = line.split(",")
    result = part_two(lines)
    print(result)


if __name__ == "__main__":
    main()
