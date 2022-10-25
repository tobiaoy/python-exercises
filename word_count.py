def count_words(filename):
    """Count the num of words in a file"""
    
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} could not be found.")
    else:
        words = content.split()
        count = len(words)
        print(f"The file {filename} has {count} words.")
        
    