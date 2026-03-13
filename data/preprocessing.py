from wordfreq import zipf_frequency
import os

#List for words in each difficulty (frequency)
easy = []
medium = []
hard = []

banned = set()
with open ('profanity_wordlist.txt', 'r') as f:
    for line in f:
        banned.add(line.strip())

with open('enable1.txt', 'r') as f:
    for line in f:
        word = line.strip()
        if len(word) < 16 and len(word) > 3 and word not in banned:
            frequency = zipf_frequency(word, 'en')
            if frequency > 5.00:
                easy.append(word)
            if frequency > 4.00:
                medium.append(word)
            if frequency > 3.10:
                hard.append(word)

with open('easy.txt', 'w') as f:
    for easyword in easy:
        f.write(easyword + "\n")

with open('medium.txt', 'w') as f:
    for mediumword in medium:
        f.write(mediumword + "\n")

with open('hard.txt', 'w') as f:
    for hardword in hard:
        f.write(hardword + "\n")