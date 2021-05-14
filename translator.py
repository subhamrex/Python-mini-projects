# pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()

sentence = '''Python is an interpreted high-level general-purpose programming language.
 Python's design philosophy emphasizes code readability with its notable use of significant indentation.'''

out = translator.translate(sentence, dest='hi')

with open("eng_to_hin.txt","w",encoding="utf-8") as f:
    f.write(out.text)

out = translator.translate("Good night Subham", dest='ja')
print(out.text)
