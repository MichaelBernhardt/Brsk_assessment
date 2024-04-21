import random
import requests

def download_word_list(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'w') as file:
            file.write(response.text)
    except requests.RequestException as e:
        print(f"Error downloading the word list: {e}")
        return False
    return True

def load_words(filename):
    word_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                key = (word[0], len(word))
                if key not in word_dict:
                    word_dict[key] = []
                word_dict[key].append(word)
    except IOError:
        print("Error loading the word file.")
        return None
    return word_dict

def process_sentence(sentence, word_dict):
    words = sentence.split()
    new_words = []
    for word in words:
        key = (word[0].lower(), len(word))
        new_word = random.choice(word_dict.get(key, [word]))
        new_words.append(new_word)
    return ' '.join(new_words)

def main():
    url = "https://github.com/dwyl/english-words/raw/master/words_alpha.txt"
    filename = "words_alpha.txt"
    if not download_word_list(url, filename):
        return
    word_dict = load_words(filename)
    if word_dict is None:
        return
    while True:
        sentence = input("Enter a sentence to process: ")
        if sentence.lower() == 'quit':
            break
        print("Processed sentence:", process_sentence(sentence, word_dict))

if __name__ == "__main__":
    main()
