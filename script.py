import spacy

nlp = spacy.load("en_core_web_lg") # NLP model installed

w1 = "red"
w2 = "walking"

w1 = nlp.vocab[w1]
w2 = nlp.vocab[w2]
print(w1.similarity(w2))

s1 = nlp("I believe in the god of the Bible")
s2 = nlp("I trust in a higher power of Christianity")
s3 = nlp("This weekend John will drink a beer")
print(s1.similarity(s2))
print(s1.similarity(s3))
print(s2.similarity(s3))

s1 = nlp("I play football in this awful arena")
s2 = nlp("I play the piano in this red room")
s3 = nlp("I repair the puano in this ugly room")
print(s1.similarity(s2))
print(s1.similarity(s3))
print(s2.similarity(s3))

s1_verbs = " ".join([token.lemma_ for token in s1 if token.pos_ == "VERB"])
print(s1_verbs)
s1_adjectives = " ".join([token.lemma_ for token in s1 if token.pos_ == "ADJ"])
print(s1_adjectives)
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