



def hostage_and_explosive_words(sentences):
    hostage_words = ['hostage', 'hostages']
    explosive_words = ['explos', 'explosive', 'explosives']
    explosive_sentences = []
    hostage_sentences = []
    sentences_without_words_suspicious = []

    for sentence in sentences:
        if any(word in sentence.lower() for word in hostage_words):
            hostage_sentences.append(sentence)
        if any(word in sentence.lower() for word in explosive_words):
            explosive_sentences.append(sentence)
        if not any(word in sentence.lower() for word in hostage_words + explosive_words):
            sentences_without_words_suspicious.append(sentence)

    return explosive_sentences, hostage_sentences, sentences_without_words_suspicious
