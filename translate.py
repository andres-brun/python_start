import googletrans
from googletrans import Translator

translator = Translator()
# print(googletrans.LANGUAGES)
print(translator.translate('Yo amo Python', dest='hi'))
