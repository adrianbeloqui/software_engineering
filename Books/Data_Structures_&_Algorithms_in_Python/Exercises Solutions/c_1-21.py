def read():
    continue_reading = True
    lines = []
    while continue_reading:
        try:
            line = lines.append(input("Enter next line or exit with ctrl+D: "))
        except EOFError:
            continue_reading = False
    
    # Two different interpretations of the question
    print("", end="\n")
    print("Reversed content:", end="\n\n")
    for line in lines:
        print("".join(list(reversed(line))))

    print("", end="\n")
    print("Reversed input order:", end="\n\n")
    for line in reversed(lines):
        print(line)

read()
