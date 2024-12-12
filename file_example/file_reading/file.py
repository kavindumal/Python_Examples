file_1 = open("file_example/file_reading/my_files.txt","w")

read_content = file_1.readlines()

print(read_content, type(read_content))

file_1.close()