import ntpath
import docx
import argparse
from enchant import Dict
from nltk.corpus import wordnet


def options():
    parser = argparse.ArgumentParser(description="Sound smarter, immediately.")
    parser.add_argument('docx_file', help="Document to babykangaroo-ify")
    return parser.parse_args()


def babykangarooify(path):
    d = Dict("en_US")
    doc = docx.Document(path)
    new_doc = docx.Document()

    for paragraph in doc.paragraphs:
        new_paragraph = []
        for word in paragraph.text.split():
            if 'joey' in word.lower():
                new_paragraph.append('baby kangaroo')
                continue
            syns = [l.name() for syn in wordnet.synsets(word) for l in syn.lemmas() if d.check(l.name())]
            if syns:
                new_word = max(syns, key=lambda s: (len(s), s))
                new_paragraph.append(new_word)
            else:
                new_paragraph.append(word)
        new_doc.add_paragraph(' '.join(new_paragraph))

    head, tail = ntpath.split(path)
    new_doc.save(head + '/bk_' + tail)


def main():
    arg = options()
    babykangarooify(arg.docx_file)


if __name__ == '__main__':
    main()
