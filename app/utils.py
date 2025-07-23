import random
import string
import base64
from typing import Optional
import itertools

# Optional (for synonym_replace)
import nltk # type: ignore
from nltk.corpus import wordnet # type: ignore

# ================= BASIC & SEEDED SCRAMBLING =================

def scramble_text_basic(text: str) -> str:
    words = text.split()
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            scrambled = word[0] + ''.join(middle) + word[-1]
        else:
            scrambled = word
        scrambled_words.append(scrambled)
    return ' '.join(scrambled_words)

def scramble_text_seeded(text: str, seed: int = 42) -> str:
    random.seed(seed)
    return scramble_text_basic(text)

# ================= CIPHERS =================

def caesar_cipher(text: str, shift: int = 3) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decipher(text: str, shift: int = 3) -> str:
    return caesar_cipher(text, -shift)

def rot13(text: str) -> str:
    return caesar_cipher(text, shift=13)

def vigenere_cipher(text: str, key: str, decrypt: bool = False) -> str:
    key = key.lower()
    key_cycle = itertools.cycle(key)
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(next(key_cycle)) - ord('a')
            k = -k if decrypt else k
            result.append(chr((ord(char) - base + k) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decipher(text: str, key: str) -> str:
    return vigenere_cipher(text, key, decrypt=True)

# ================= TRANSFORMATIONS =================

def reverse_text(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split())

def pig_latin(text: str) -> str:
    def convert_word(word):
        if not word:
            return word
        first_letter = word[0]
        if first_letter.lower() in 'aeiou':
            return word + "yay"
        else:
            for i, char in enumerate(word):
                if char.lower() in 'aeiou':
                    return word[i:] + word[:i] + "ay"
            return word + "ay"
    return ' '.join(convert_word(word) for word in text.split())

# ================= ENCODINGS =================

def base64_encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def base64_decode(encoded_text: str) -> str:
    try:
        return base64.b64decode(encoded_text.encode()).decode()
    except Exception:
        return "[Invalid base64 input]"

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/', ',': '--..--', '.': '.-.-.-', '?': '..--..'
}
MORSE_REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_encode(text: str) -> str:
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morse_decode(morse_code: str) -> str:
    words = morse_code.strip().split(' ')
    decoded = ''.join(MORSE_REVERSE_DICT.get(code, '') for code in words)
    return decoded.replace('/', ' ')

def binary_encode(text: str) -> str:
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decode(binary_text: str) -> str:
    try:
        return ''.join(chr(int(b, 2)) for b in binary_text.split())
    except Exception:
        return "[Invalid binary input]"

# ================= NON-REVERSIBLE STYLISTIC =================

def leet_speak(text: str) -> str:
    replacements = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'}
    return ''.join(replacements.get(c.lower(), c) for c in text)

def emoji_replace(text: str) -> str:
    mapping = {
        'happy': '😊', 'sad': '😢', 'love': '❤️', 'fire': '🔥', 'star': '⭐',
        'money': '💰', 'cool': '😎', 'heart': '💖'
    }
    return ' '.join(mapping.get(word.lower(), word) for word in text.split())

# ================= NLP Synonym Replacement =================

def synonym_replace(text: str) -> str:
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
    words = text.split()
    new_words = []
    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            lemmas = synonyms[0].lemma_names()
            new_word = lemmas[0].replace('_', ' ') if lemmas else word
            new_words.append(new_word)
        else:
            new_words.append(word)
    return ' '.join(new_words)
