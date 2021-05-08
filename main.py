# importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

sentence = "saya bangga jadi warga nahdlatul ulama"
words = word_tokenize(sentence)

for w in words:
	print(w, " : ", ps.stem(w))

