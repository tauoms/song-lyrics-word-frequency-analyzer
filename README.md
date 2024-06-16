# Song Lyrics Word Frequency Analyzer

A program that takes input song lyrics and outputs a graph of the most frequently used words and a text file of all unique (appears only once) words used. Input lyrics can be a song, an album or the whole discography of an artist.

The file "excluded_words.txt" has some common stop words that are filtered out from results. These can be modified by the user.

## Technologies used

Built with:

- Python
  - nltk (Natural Language Toolkit)
  - matplotlib.pyplot
  - numpy

## Setup and usage

#### Prerequisites

Python Installation: Ensure Python 3.x is installed on your system. You can download it from python.org or manage it via a package manager like brew on macOS or Linux.

Install virtualenv if not already installed:

```
pip install virtualenv
```

#### Clone the Repository

```
git clone https://github.com/tauoms/song-lyrics-word-frequency-analyzer.git
cd song-lyrics-word-frequency-analyzer
```

#### Create a virtual environment (assuming venv as the name):

```
python3 -m venv .venv
```

#### Activate the virtual environment:

Linux/macOS:

```
source .venv/bin/activate
```

Windows (using Command Prompt):

```
.venv\Scripts\activate
```

Or (using PowerShell):

```
.venv\Scripts\Activate.ps1
```

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Input your lyrics

Input lyrics (song/album/discography) into "input_here.txt". Lines starting with number (i.e "2. Second Son of R) are excluded by the program to make it easier to paste whole album lyrics from lyric websites.

#### Run the Python Program

```
python main.py
```

## Screenshot

```

```
