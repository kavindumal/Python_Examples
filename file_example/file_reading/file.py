file_1 = open("file_example/file_reading/my_file.txt","r")

read_content = file_1.readline()

print(read_content, type(read_content))

file_1.close()