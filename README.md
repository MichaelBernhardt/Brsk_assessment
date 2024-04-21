Scrabble Helper

Scrabble Helper is a Python tool designed to help Scrabble players enhance their game by transforming sentences. Given any sentence, the tool substitutes each word with a random word that starts with the same letter and has the same length, if such a word exists. If no replacement is found, the original word is retained. This transformation process helps in brainstorming and word association practice for Scrabble players.
Prerequisites

Before you begin, ensure you have met the following requirements:

    You have Python 3 or higher installed on your machine.

Installing Scrabble Helper

To install Scrabble Helper, follow these steps:

Linux and macOS:

bash

git clone https://your-repository-url.git
cd name-of-the-repository
python3 -m venv venv
source venv/bin/activate
pip install requests

Windows:

bash

git clone https://your-repository-url.git
cd name-of-the-repository
python -m venv venv
.\venv\Scripts\activate
pip install requests

Using Scrabble Helper

To use Scrabble Helper, follow these steps:

bash

python scrabble_helper.py # Use 'python3' on macOS and Linux

After running the command, the program will prompt you to enter a sentence. Type your sentence and press Enter to see the transformed output. Repeat as needed. To exit, type quit and press Enter.