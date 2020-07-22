# 1st task:
# par 1 ↓
# with open('hw_08_(1)', 'r') as main_file:
#     print(main_file.read())


# par 2 ↓
# with open('hw_08_(1)', 'r') as main_file, open('hw_08_(2)', 'w') as file_to_write:
#     data = main_file.read()
#     file_to_write.write(read)


# par 3 ↓
def read_this(file):
    for i in file.readlines():
        i = str(i)
    file.write('or not read\nso, i don\'t care')
    return file


# with open('hw_08_(1)', 'r') as main_file, open('hw_08_(2)', 'w') as file_to_write:
#     data = main_file.read()
#     file_to_write.write(data)


# with open('hw_08_(2)', 'r+') as file_to_write:
#     read_this(file_to_write)


# 2d task:
import json


# with open('questions.json', 'r') as json_file:
#     data = json.load(json_file)
#     for q in data['questions']:
#         q['answer'] = input(q['q'] + '\n>')


# with open('questions.json', 'w') as json_file:
#     json.dump(data, json_file, indent = 4)


# 3d task:
