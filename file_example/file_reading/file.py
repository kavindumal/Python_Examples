# r - Open a file for reading
# w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x - Open a file for exclusive creation. If the file already exists, the operation will fail.
# a - Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t - Open in text mode. (default)

with open('file_example/file_reading/my_file_1.txt', 'w') as file:
    file.writelines(['This is something new.\n', 'This is writelines method\n'])