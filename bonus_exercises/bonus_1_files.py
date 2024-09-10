contents = ["Carrots to be cut square",
            "Carrots reported to have been cut square",
            "Carrots presented cut square"]

filenames = ['doc.txt', 'presentation.txt', 'report.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../text-files/{filename}", "w")
    file.write(content)
    file.close()

    file = open(f"../text-files/{filename}", "r")
    file_content = file.read()
    print(file_content)
    file.close()