def correct_sentence(sentence1, sentence2):
    sentences = [sentence1, sentence2]
    corrected_sentences = []
    for sentence in sentences:
        if not sentence.endswith("."):
            sentence += "."
        corrected_sentences.append(sentence.capitalize())
    return " ".join(corrected_sentences)
print(correct_sentence("please note that not all fixes are necessary", "If the sentence AlreaDy ends with a full stop, you don't Need to adD another one, IT would be a mistake."))
