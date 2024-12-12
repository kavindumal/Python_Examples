# r - Open a file for reading
# w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x - Open a file for exclusive creation. If the file already exists, the operation will fail.
# a - Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t - Open in text mode. (default)

with open('file_example/file_reading/my_file.txt', 'r') as file:
    content = file.read()
    print(content)
    
# No needs for file.close() as it's handle automatically by the with statement