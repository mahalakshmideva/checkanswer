from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer	#Importing module for sentence tokenisation
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
tokenizer = RegexpTokenizer("[\w']+")		#Function to tokenise from regular expression
lemmatizer = WordNetLemmatizer()
sentence="You would need to add materials that you need to use. You also would want to know how much vinegar you should pour in the cups. You should also say what you should label the container with if it should be the sample or letters like A"

arr = []
arr1 = []
sentence=tokenizer.tokenize(sentence)

for i in sentence:
 j=stemmer.stem(i)
 arr.append(j)
 k=lemmatizer.lemmatize(i)
 arr1.append(k)

print(sentence)
print('\n')
print("--------------------------------------------------------")
print('\n')
print(arr)
print('\n')
print("*********************************************************")
print('\n')
print(arr1)
