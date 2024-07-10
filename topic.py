#word tokenization
put = input("Input word: ")
list = []
sentence = ""

for i in put:
    if i == " ":
        list.append(sentence)
        sentence = ""
    else:
        sentence += i
list.append(sentence)
print(list)