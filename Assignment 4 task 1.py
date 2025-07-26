try:
    file=open('sample.txt','r')

    print("Reading file content:")
    print(f"Line 1:{ file.readline().strip()}")
    print(f"Line 2: {file.readline().strip()}")
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
