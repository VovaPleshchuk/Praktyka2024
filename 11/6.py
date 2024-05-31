def check_sequence(sequence):
    i = 0
    n = len(sequence)

    while i < n:
        if sequence[i] == '0':

            zero_count = 0
            while i < n and sequence[i] == '0':
                zero_count += 1
                i += 1

            one_count = 0
            while i < n and sequence[i] == '1':
                one_count += 1
                i += 1

            if zero_count != one_count:
                return False
        else:
            i += 1

    return True

print(check_sequence("01010101"))
print(check_sequence("00011100011"))

