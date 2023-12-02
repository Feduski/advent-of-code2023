input_file = open("input.txt", "r")
input_data = input_file.read()
input_file.close()

total = 0
line_value = 0
dicc_real_numbers = {'eighthree':'83','oneight':'18', 'eightwo': '82', 'twone':'21', 'threeight': '38', 'fiveight': '58',
                       'sevenine': '79', 'nineight':'98', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
                       } 
#I added the first ones because I noticed that the input had some numbers written together.

for line in input_data.splitlines():
    print('original line', line)
    real_number_per_line = []
    for written_number in dicc_real_numbers.keys():
        if written_number in line:
            line = line.replace(written_number, dicc_real_numbers[written_number])
    for caracter in line:
        if not caracter.isdigit():
            line = line.replace(caracter, '')
    line_value = line[0] + line[-1]
    total += int(line_value)
    line_value = 0
    print('line after replace', line)

print(total)