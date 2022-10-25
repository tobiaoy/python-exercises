files = ['odyssey.txt', 'monte_cristo.txt', 'faust.txt']

def count_word(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.lower().split()
        count = words.count(word)
        print(f"The word {word} appears {count} times in {filename}.")
        
for file in files:
    count_word(file, 'the')