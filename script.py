import os
import socket

# fecthing ip address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# function to read file


def readfile(file):
    with open(file, 'r') as f:
        text = f.read()
        words = text.split()
        return words


# getting the word count from the files in data folder
textfiles = os.listdir('/home/data')
top_words = {}
word_count = []
for file in textfiles:
    filepath = os.path.join('/home/data', file)
    words = readfile(filepath)
    word_count.append(len(words))
    if file == "IF.txt":
        words = readfile(filepath)
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        top_words = sorted([(word, count) for word, count in word_dict.items(
        )], key=lambda x: x[1], reverse=True)[:3]

# writing to the result file
with open('/home/output/result.txt', 'w') as file:
    file.write("text files: \n")
    for name in textfiles:
        file.write(f'{name}\n')
    file.write("\n\n")
    file.write("word count for each text file: \n")
    for i in range(len(word_count)):
        file.write(f'{textfiles[i]} : {word_count[i]}\n')

    file.write(f'\nGrand total: {sum(word_count)}\n\n')
    file.write('Top 3 words with maximum count in IF.txt:\n')
    for word, freq in top_words:
        file.write(f'{word}: {freq}\n')
    file.write(f'\nIP address: {ip_address}')

# displaying the result file
with open('/home/output/result.txt', 'r') as file:
    print(file.read())
