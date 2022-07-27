if not __name__ == "__main__":
    exit("ERROR: The MAL interpreter should not be run as a library!")

f = open('code.bin', 'r')
while f:
    stringcheck = f.readline(100000)
    checkpoint= stringcheck[:1]
    checkend= stringcheck[:3]

    if checkpoint == '.':
        replacepoint = stringcheck.replace('.', '')
        replacespace = replacepoint.replace('\n', '')
        print (replacespace)
    if checkend == 'END':
            f.close()
            break

