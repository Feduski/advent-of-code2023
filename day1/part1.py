input_file = open("input.txt", "r")
input_data = input_file.read()
input_file.close()

total = 0
line_value = 0

for line in input_data.splitlines():
    numbers_in_line = []
    for caracter in line:
        if caracter.isnumeric():
            numbers_in_line.append(caracter)
    line_value = numbers_in_line[0] + numbers_in_line[-1]
    total += int(line_value)
    numbers_in_line = []
    line_value = 0

print(total)