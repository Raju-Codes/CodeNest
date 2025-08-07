try:
    fileName = 'mytext.txt'
    file = open(fileName,'r')
    count = 1
    print("Reading file content:")
    for line in file:
        print(f"Line {count}:",line.strip())
        count=count+1;
except(FileNotFoundError):
    print(f"Error: The file '{fileName}' was not found.")