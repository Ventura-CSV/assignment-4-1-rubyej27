def main():
    result = []
    while True:
        start = input('Enter the starting letter: ').lower()
        end = input('Enter the starting letter: ').lower()
        if not (start.isalpha() and end.isalpha()):
            print("Error: Both inputs must be letters.")
            continue
        if len(start) != 1 or len(end) != 1:
            print("Error: both must be single letters.")
            continue
        if ord(start) > ord(end):
            print("Error: the start letter must be less than the end letter.")
            continue
        break
    for char_code in range(ord(start), ord(end) + 1):
        result.append(chr(char_code))
    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
