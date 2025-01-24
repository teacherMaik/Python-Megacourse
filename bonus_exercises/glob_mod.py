import glob

#Return a list of paths matching a pathname pattern.
myfiles = glob.glob('../text-files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())


