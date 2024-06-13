from collections import Counter
import re

def process_lyrics(file_path, excluded_words_path):
    
    # Read the excluded words
    with open(excluded_words_path, 'r') as file:
        excluded_words = set(file.read().strip().lower().split(','))

    # Read the file
    with open(file_path, 'r') as file:
        lyrics = file.read()
    
    # Clean and split the text into words
    # Convert to lowercase and use regex to find words
    words = re.findall(r'\b\w+\b', lyrics.lower())
    
    # Filter out excluded words
    words = [word for word in words if word not in excluded_words]

    # Count word frequencies
    word_counts = Counter(words)
    
    # Find the most frequently occurring words
    most_common_words = word_counts.most_common()
    
    # Find unique words (those that appear only once)
    unique_words = [word for word, count in word_counts.items() if count == 1]
    
    return most_common_words, unique_words

def main():
    file_path = 'input_here.txt'
    excluded_words_path = 'excluded_words.txt'
    most_common_words, unique_words = process_lyrics(file_path, excluded_words_path)
    
    print("Most Frequently Occurring Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    
    print("\nUnique Words (Appear Only Once):")
    print(unique_words)

if __name__ == "__main__":
    main()
