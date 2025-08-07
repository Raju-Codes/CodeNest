try:
    fileName='output.txt'
    text = input('Enter text to write to the file: ')
    file = open(fileName,'w+')
    file.write(text+'\n')
    file.close()
    print(f'Data successfully written to {fileName}.\n')

    text = input('Enter additional text to append: ')
    file = open(fileName,'a')
    file.write(text+'')
    file.close()
    print('Data successfully appended.\n')

    print(f'Final content od {fileName}:')
    file = open(fileName,'r')
    print(file.read())
    file.close()

except FileNotFoundError:
    print(f"Error: the file 'fileName' was not found.")