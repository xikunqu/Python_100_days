from translate import Translator

to_transla='''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
'''
translator=Translator(to_lang="chinese")
translation=translator.translate(to_transla)
print(translation)