# README

## Overview

This script demonstrates the use of the spaCy library for various Natural Language Processing (NLP) tasks, showcasing functionalities such as loading a pre-trained NLP model, calculating word and sentence similarities, and extracting specific parts of speech (verbs, adjectives, and nouns) from sentences.

## Requirements

- Python 3.x
- spaCy library
- Pre-trained spaCy model: `en_core_web_lg`

## Installation

1. Install spaCy:
    ```bash
    pip install spacy
    ```

2. Download the `en_core_web_lg` model:
    ```bash
    python -m spacy download en_core_web_lg
    ```

## Usage

1. **Loading the NLP Model:**
    ```python
    import spacy

    nlp = spacy.load("en_core_web_lg")
    ```

2. **Word Similarity:**
    The script calculates the similarity between two words.
    ```python
    w1 = nlp.vocab["red"]
    w2 = nlp.vocab["walking"]
    print(w1.similarity(w2))
    ```

3. **Sentence Similarity:**
    The script calculates the similarity between pairs of sentences.
    ```python
    s1 = nlp("I believe in the god of the Bible")
    s2 = nlp("I trust in a higher power of Christianity")
    s3 = nlp("This weekend John will drink a beer")
    
    print(s1.similarity(s2))
    print(s1.similarity(s3))
    print(s2.similarity(s3))
    ```

4. **Extracting Lemmas:**
    The script extracts and prints the lemmas of verbs, adjectives, and nouns from the sentences.
    ```python
    s1 = nlp("I play football in this awful arena")
    s2 = nlp("I play the piano in this red room")
    s3 = nlp("I repair the piano in this ugly room")

    # Extracting verbs
    s1_verbs = " ".join([token.lemma_ for token in s1 if token.pos_ == "VERB"])
    print(s1_verbs)

    # Extracting adjectives
    s1_adjectives = " ".join([token.lemma_ for token in s1 if token.pos_ == "ADJ"])
    print(s1_adjectives)

    # Extracting nouns
    s1_nouns = " ".join([token.lemma_ for token in s1 if token.pos_ == "NOUN"])
    print(s1_nouns)

    s2_verbs = " ".join([token.lemma_ for token in s2 if token.pos_ == "VERB"])
    print(s2_verbs)

    s2_adjectives = " ".join([token.lemma_ for token in s2 if token.pos_ == "ADJ"])
    print(s2_adjectives)

    s2_nouns = " ".join([token.lemma_ for token in s2 if token.pos_ == "NOUN"])
    print(s2_nouns)

    s3_verbs = " ".join([token.lemma_ for token in s3 if token.pos_ == "VERB"])
    print(s3_verbs)

    s3_adjectives = " ".join([token.lemma_ for token in s3 if token.pos_ == "ADJ"])
    print(s3_adjectives)

    s3_nouns = " ".join([token.lemma_ for token in s3 if token.pos_ == "NOUN"])
    print(s3_nouns)
    ```

## Example Output

The script provides the following example outputs:

1. Word similarity between "red" and "walking".
2. Sentence similarities between the provided sentence pairs.
3. Lemmas of verbs, adjectives, and nouns extracted from the provided sentences.

## Notes

- The similarity scores are floating-point values between 0 and 1, where 1 indicates identical meaning and 0 indicates no similarity.
- The extraction of lemmas is conducted based on the part-of-speech tagging provided by the spaCy model.

This script is designed for educational purposes to illustrate the capabilities of the spaCy library in handling various NLP tasks effectively.
