import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter

# Ensure you download necessary nltk data files
nltk.download('punkt')
nltk.download('wordnet')

def read_excluded_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        excluded_words = file.read().strip().split(',')
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
    
    # Remove punctuation marks except comma
    text = re.sub(r'[^\w\s,]', '', text)
    
    return text

def process_lyrics(file_path, excluded_words, min_word_count=5):
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Read the lyrics file
    with open(file_path, 'r', encoding='utf-8') as file:
        lyrics = file.read()
    
    # Preprocess the text to normalize contractions and handle punctuation
    lyrics = preprocess_text(lyrics.lower())
    
    # Tokenize the text into words
    words = word_tokenize(lyrics)
    
    # Lemmatize the words and filter out excluded words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word.strip() and word.lower() not in excluded_words]
    
    # Count word frequencies
    word_counts = Counter(lemmatized_words)
    
    # Filter words by minimum count
    filtered_words = {word: count for word, count in word_counts.items() if count >= min_word_count and word != ','}
    
    # Sort by frequency in descending order
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    
    # Find unique words (those that appear only once)
    unique_words = [word for word, count in word_counts.items() if count == 1 and word.lower() not in excluded_words and word != ',']
    
    return sorted_words, unique_words

def plot_most_common_words(words_freq, min_word_count, unique_words):
    # Filter words that meet the minimum count threshold
    words_freq = [(word, freq) for word, freq in words_freq if freq >= min_word_count]
    
    # Extract words and frequencies
    words = [word for word, freq in words_freq]
    frequencies = [freq for word, freq in words_freq]
    
    # Plotting horizontal bar chart
    plt.figure(figsize=(10, 8))
    bars = plt.barh(words, frequencies, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Most Common Words (Minimum Count >= {min_word_count})')
    plt.gca().invert_yaxis()  # Invert y-axis to have the most common word at the top
    
    # Annotate bars with exact counts
    for bar, frequency in zip(bars, frequencies):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{frequency}', 
                 ha='left', va='center', fontsize=10, color='black')
    
    # Display unique words list below the plot, aligned to the left
    unique_text = ', '.join(unique_words)  # Create comma-separated list
    plt.text(0.02, -0.2, f'Unique Words: {unique_text}', transform=plt.gca().transAxes,
             fontsize=12, ha='left', va='top', bbox=dict(facecolor='lightgray', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

def main():
    lyrics_file_path = 'input_here.txt'  # File path for the lyrics
    excluded_words_path = 'excluded_words.txt'  # File path for the excluded words
    min_word_count = 2  # Minimum count of a word to be considered as most common
    
    # Read excluded words
    excluded_words = read_excluded_words(excluded_words_path)
    
    # Process lyrics
    most_common_words, unique_words = process_lyrics(lyrics_file_path, excluded_words, min_word_count)
    
    # Print most common words
    print(f"Most Frequently Occurring Words (minimum count >= {min_word_count}):")
    for word, count in most_common_words:
        print(f"{word}: {count}")
    
    # Plot most common words
    plot_most_common_words(most_common_words, min_word_count, unique_words)
    
    # Print unique words as comma-separated list
    print("\nUnique Words (Appear Only Once After Filtering):")
    print(', '.join(unique_words))

if __name__ == "__main__":
    main()
