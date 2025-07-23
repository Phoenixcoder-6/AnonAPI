# AnonAPI
AnonAPI is a lightweight and modular FastAPI-based web service designed to scramble, encrypt, and decrypt text data securely and efficiently. Ideal for developers building anonymization, obfuscation, or text protection tools in applications ranging from testing to privacy-focused deployments.

# 🕵️‍♂️ AnonAPI - Text Scrambler & Decryption Microservice

AnonAPI is a privacy-focused, FastAPI-powered microservice designed for scrambling and unscrambling text data. It allows developers and testers to anonymize sensitive information quickly and securely via a RESTful API. Perfect for use in data masking, testing pipelines, secure logging, or any situation where text obfuscation is required.

---

## 🚀 Project Goals

- ✅ Build a lightweight API to scramble and unscramble sensitive text.
- ✅ Enable easy integration into any service using simple HTTP endpoints.
- ✅ Ensure the application is containerized and production-ready using Docker.
- ✅ Provide flexible text processing with features like:
        - Character-level scrambling
        - Word-level scrambling
        - Sentence-level permutation
        - Reversible unscrambling (optional, using deterministic methods)


## 💡 Why AnonAPI?

In many real-world applications, especially in testing or demo environments, exposing real user or sensitive data can violate compliance rules (like GDPR, HIPAA). AnonAPI is designed to:

- 🛡 Protect real data by obfuscating it
- 🔁 Reverse scrambling when needed
- ⚙️ Easily deploy and integrate with other tools
- 🐳 Run in isolated environments using Docker

---

## 🧠 Features
<img width="833" height="291" alt="image" src="https://github.com/user-attachments/assets/5513f295-2515-4865-806b-f3d944021e95" />

---

## 🏗 Folder Structure

<img width="588" height="353" alt="image" src="https://github.com/user-attachments/assets/9a1ea1ee-8025-46c9-88cd-6f6b0b6017f8" />

---

## 🔠 Supported Scrambling Models

-- 1. Basic

- Description: Returns the input text as-is, with no modification.
- Example:


                Input:  Hello World
                Output: Hello World


- 2. seeded

- Description: Produces a consistent random shuffling of characters based on a fixed seed value.
- Example:

         Input:     Hello
         Seed:      42
         Output:    loHel  (consistent for seed=42)


- 3. caesar

- Description: Applies a Caesar cipher by shifting each letter by a fixed number of positions in the alphabet.
- Example:
  
        Input:     Hello
        Shift:     3
        Output:    Khoor

- 4. rot13

- Description: A special case of Caesar cipher with a fixed shift of 13.
- Example:

        Input:     Hello
        Output:    Uryyb

- 5. reverse

- Description: Reverses the input string.

- Example:


        Input:     Hello
        Output:    olleH


- 6. piglatin
Description: Converts English words into Pig Latin.

Example:

text
Copy
Edit
Input:     Hello World
Output:    elloHay orldWay
7. vigenere
Description: Applies the Vigenère cipher using a keyword.

Example:

text
Copy
Edit
Input:     Hello
Keyword:   key
Output:    Rijvs
8. base64
Description: Encodes the input text to Base64 format.

Example:

text
Copy
Edit
Input:     Hello
Output:    SGVsbG8=
9. morse
Description: Translates text to Morse code.

Example:

text
Copy
Edit
Input:     Hello
Output:    .... . .-.. .-.. ---
10. binary
Description: Converts each character to its binary (ASCII) representation.

Example:

text
Copy
Edit
Input:     Hi
Output:    01001000 01101001
11. leet
Description: Converts text to "leet speak" (1337), replacing letters with look-alike numbers or symbols.

Example:

text
Copy
Edit
Input:     Hello
Output:    H3ll0
12. synonym
Description: Replaces words with their synonyms using an NLP library like WordNet.

Example:

text
Copy
Edit
Input:     Fast runner
Output:    Quick sprinter
13. emoji
Description: Translates words or concepts into emojis when possible.

Example:

text
Copy
Edit
Input:     I love pizza
Output:    I ❤️ 🍕

## ⚙️ Features

- ✅ Scramble API

  Accepts plain text and scrambles predefined sensitive entities (names, locations, etc.).
  Returns scrambled version along with mapping key.

- ✅ Descramble API

  Accepts scrambled text and a mapping key to return the original text.
  Helpful for reversible anonymization during debugging or controlled testing.

- ✅ NLTK Support

  Uses NLTK models (e.g., named entity recognition) to identify PII.

- ✅ Regex-based Fallback

  For cases where NLTK fails, regex-based matching ensures fallback anonymization.

- ✅ Modular Design

  Code is cleanly separated into modules for app logic, routing, and utility functions.

- ✅ Dockerized Deployment

  Container-ready for easy deployment using:

        docker build -t fastapi-scrambler .
        docker run -d -p 8000:8000 fastapi-scrambler

- ✅ Test Files Support

  Includes test_files/ folder with sample inputs for local experiments.

---

## 🛠️ Installation and Setup

- Clone the Repo
  
        git clone https://github.com/your-username/data-scrambler-api.git
        cd data-scrambler-api
  
- Install Dependencies
        
        pip install -r requirements.txt
        python nltk_setup.py

- Run Locally

        uvicorn app.main:app --reload
        Visit: http://localhost:8000/docs for Swagger UI.

- 🐳 Run with Docker

        docker build -t fastapi-scrambler .
        docker run -d -p 8000:8000 fastapi-scrambler


---

## 🧪 Sample Files

Use files inside test_files/ for testing the API endpoints with real-world examples.

## 🔐 Security & Limitations

- Only anonymizes named entities (persons, locations, dates).
- You can extend it to support emails, phone numbers, or custom regex patterns.
- Key mappings are stored in-memory or passed externally — ensure security in real deployments.






