import os
import nltk
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def preprocess_text(text, print_steps=False):

    if print_steps:
        print("Original text:\n", text) 
    
    text = text.lower()
    if print_steps:
        print("\nAfter lowercase:\n", text)
    
    tokens = word_tokenize(text)
    if print_steps:
        print("\nAfter tokenization:\n", ' '.join(tokens))  
    
    tokens = [token for token in tokens if token.isalpha()]
    if print_steps:
        print("\nAfter removing punctuation and blank space tokens:\n", ' '.join(tokens))
    
    tokens = [token for token in tokens if token not in stop_words]
    if print_steps:
        print("\nAfter removing stopwords:\n", ' '.join(tokens))
    
    processed_text = ' '.join(tokens)
    return processed_text

folder_path = '/Users/mj/Desktop/Work/Sem6/IR/IRAssignment/text_files'
new_folder_path = '/Users/mj/Desktop/Work/Sem6/IR/IRAssignment/newtextfiles'
sample_files = random.sample(range(1, 1000), 5)  

for i in range(1, 1000):
    file_path = os.path.join(folder_path, f'file{i}.txt')
    new_file_path = os.path.join(new_folder_path, f'newfile{i}.txt')
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            print_steps = i in sample_files
            if print_steps:
                print(f"\nProcessing and printing transitions for file{i}.txt...")
            processed_text = preprocess_text(text, print_steps=print_steps)
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(processed_text)
