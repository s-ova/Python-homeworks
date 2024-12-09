def correct_sentence(sentence):
    sentences = sentence.split('. ')
    corrected_sentences = []
    for s in sentences:
        s = s.strip()  
        if s:
            if not s.endswith('.'):
                s += '.'
            corrected_sentences.append(s.capitalize())
    return ' '.join(corrected_sentences)
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')