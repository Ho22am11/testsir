from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

text = input("Enter some text: ")
print("Choose an option:")
print("1. Print tokenized words")
print("2. Print tokenized sentences")
print("3. Print original text")
print("4. Stemming")
choice = int(input("enter choice number: "))
if choice == 1:
      words = word_tokenize(text)
      print(words)
elif choice == 2:
      sentences = sent_tokenize(text)
      print(sentences)
elif choice == 3:
      print(text)
elif choice == 4:
      print("Choose a stemming algorithm:")
      print("1. Porter Stemmer")
      print("2. Snowball Stemmer")
      stem_choice = int(input("enter your choice stem number:"))
      if stem_choice == 1:
            porter_stemmer = PorterStemmer()
            words = word_tokenize(text)
            stemmed_words = [porter_stemmer.stem(word) for word in words]
            print("PorterStemmer", stemmed_words)
      elif stem_choice == 2:
            snowball_stemmer = SnowballStemmer(language='english')
            words = word_tokenize(text)
            stemmed_words = [snowball_stemmer.stem(word) for word in words]
            print( "SnowballStemmer",stemmed_words)
else:
      print("Invalid Choice")