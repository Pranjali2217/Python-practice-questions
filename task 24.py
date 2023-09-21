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

with open('sentences.txt','r')as input_file, open('reversed_sentences.txt','w') as output_file:
    for line in input_file:
        reversed_sentence=line[::-1]
        output_file.write(reversed_sentence + '/n')

print("reversed sentences have been written to reversed_sentences.txt")

