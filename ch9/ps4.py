word = ["gogi", "tapu"]

with open("demo1.txt") as f:
    content = f.read()

for words in word:
    content = content.replace(words, "$" * len(word))

with open("demo1.txt", "w") as f:
    f.write(content)