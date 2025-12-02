def update_base(base: int, val: int) -> int:
    new_val = base + val
    return new_val % 100


def main():
    base = 50
    counter = 0
    with open("day1.txt") as file:
        for line in file:
            direction = line[0]
            val = int(line[1:])
            match direction:
                case "R":
                    inc = (base + val) // 100
                    base = (base + val) % 100
                    counter += inc - 1 if inc > 0 and base == 0 else inc
                case "L":
                    inc = abs((base - val) // 100)
                    counter += inc - 1 if inc > 0 and base == 0 else inc
                    base = (base - val) % 100
                case _:
                    assert False
            if base == 0:
                counter += 1
            print(counter, line)

    print(f"Result = {counter}")


if __name__ == "__main__":
    main()
