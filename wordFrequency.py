print("precaution: andika herufi ndogo tu halafu usiweke punctuations")
text = input("write words: ").strip()
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nMatokeo ya idadi ya maneno:")
for word, count in frequency.items():
    print(f"{word}: {count}")