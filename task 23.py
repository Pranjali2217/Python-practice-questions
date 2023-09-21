sentences = []
while True:
    sentence = input("Enter a as many sentences as you want (or press Enter to finish): ")
    if sentence:
        sentences.append(sentence)
    else:
        break

file=open('sentences.txt','w')
for sentence in sentences:
    file.write(sentence + "\n")
print("Sentences have been written to 'sentences.txt'.")
file.close()