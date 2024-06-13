from collections import Counter
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure you download necessary nltk data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def read_and_sort_excluded_words(file_path):
    # Read the excluded words
    with open(file_path, 'r') as file:
        excluded_words = file.read().strip().lower().split(',')
    
    # Strip any whitespace from the words in the excluded list and sort them
    excluded_words = sorted({word.strip() for word in excluded_words})
    
    # Write the sorted excluded words back to the file
    with open(file_path, 'w') as file:
        file.write(', '.join(excluded_words))
    
    return set(excluded_words)

def preprocess_text(text):
    # Normalize contractions and possessives
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"'re", " are", text)
    text = re.sub(r"'s", " is", text)
    text = re.sub(r"'d", " would", text)
    text = re.sub(r"'ll", " will", text)
    text = re.sub(r"'t", " not", text)
    text = re.sub(r"'ve", " have", text)
    text = re.sub(r"'m", " am", text)
    
    return text

def process_lyrics(file_path, excluded_words):
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Read the lyrics file
    with open(file_path, 'r') as file:
        lyrics = file.read()
    
    # Preprocess the text to normalize contractions
    lyrics = preprocess_text(lyrics.lower())
    
    # Tokenize the text into words
    words = word_tokenize(lyrics)
    
    # Lemmatize the words and filter out excluded words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in excluded_words]
    
    # Count word frequencies
    word_counts = Counter(lemmatized_words)
    
    # Find the most frequently occurring words
    most_common_words = word_counts.most_common()
    
    # Find unique words (those that appear only once)
    unique_words = [word for word, count in word_counts.items() if count == 1]
    
    return most_common_words, unique_words

def main():
    lyrics_file_path = 'input_here.txt'  # File path for the lyrics
    excluded_words_path = 'excluded_words.txt'  # File path for the excluded words
    
    # Read and sort the excluded words
    excluded_words = read_and_sort_excluded_words(excluded_words_path)
    
    # Process the lyrics
    most_common_words, unique_words = process_lyrics(lyrics_file_path, excluded_words)
    
    print("Most Frequently Occurring Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    
    print("\nUnique Words (Appear Only Once):")
    print(unique_words)

if __name__ == "__main__":
    main()
