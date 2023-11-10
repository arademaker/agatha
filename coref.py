
import spacy

nlp = spacy.load("en_core_web_sm")

assert "transformer" not in nlp.pipe_names
nlp_coref = spacy.load("en_coreference_web_trf")
nlp.add_pipe("transformer", source=nlp_coref)
nlp.add_pipe("coref", source=nlp_coref)
nlp.add_pipe("span_resolver", source=nlp_coref)
nlp.add_pipe("span_cleaner", source=nlp_coref)


# Examples from https://en.m.wikipedia.org/wiki/Coreference

sentences = [
    "The music was so loud that it couldn't be enjoyed.",
    'Our neighbors dislike the music. If they are angry, the cops will show up soon. ',
    'If they are angry about the music, the neighbors will call the cops.',
    'Carol told Bob to attend the party. They arrived together.',
    'When Carol helps Bob and Bob helps Carol, they can accomplish any task.',
    'The project leader is refusing to help. The jerk thinks only of himself.',
    'Some of our colleagues are going to be supportive. These kinds of people will earn our gratitude.']

for s in sentences:
    print("sentence:", s)
    doc = nlp(s)
    for k,v in doc.spans.items():
        print('cluster:', k)
        for vi in v:
            print('item:', vi, vi.start_char, vi.end_char)

txt = "Someone who lives in Dreadbury Mansion killed Aunt Agatha. Agatha, the butler, and Charles live in Dreadbury Mansion, and are the only people who live therein. A killer always hates his victim, and is never richer than his victim. Charles hates no one that Aunt Agatha hates. Agatha hates everyone except the butler. The butler hates everyone not richer than Aunt Agatha. The butler hates everyone Aunt Agatha hates. No one hates everyone. Agatha is not the butler. Therefore, Agatha killed herself."


doc = nlp(txt)
for s in doc.sents:
    print(s,s.start_char, s.end_char)
for k,v in doc.spans.items():
    print('cluster:', k)
    for vi in v:
        print('item:', vi, vi.start_char, vi.end_char)
    
    


