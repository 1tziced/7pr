def process_line(line, line_number):
    words = line.split('-')
    last_word = words[-1]
    first_letter = last_word[0].lower()

    filtered_words = {word for word in words if first_letter in word.lower()}
    sorted_words = sorted(filtered_words, key=str.lower)
    result = " ".join(sorted_words)

    if len(result) % line_number == 0:
        result = result.title()
    else:
        result = result.lower()

    print(result)



def main():
    line_number = 1
    while True:
        line = input().strip()
        if line == "42":
            break
        process_line(line, line_number)
        line_number += 1


if __name__ == "__main__":
    main()