def inputt(inputq):
    return set(map(int, inputq.split(', ')))


def find_common_numbers(set1, set2, set3):
    return set1 & set2 & set3


def print_results(common_numbers):
    if common_numbers:
        print(" ".join(map(str, sorted(common_numbers))))
        print(max(common_numbers))
    else:
        print()



def main():
    input_str1 = input().strip()
    input_str2 = input().strip()
    input_str3 = input().strip()

    set1 = inputt(input_str1)
    set2 = inputt(input_str2)
    set3 = inputt(input_str3)

    common_numbers = find_common_numbers(set1, set2, set3)
    print_results(common_numbers)


if __name__ == "__main__":
    main()
