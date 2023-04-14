import re
# Define documents ////
docs = {
      ' 1': ' new home sales top forecasts ',
      ' 2': ' home sales rise in july ',
      ' 3': ' increase in home sales in july ',
      ' 4': ' july new home sales rise '
}

# Define stop words ////
stop_words = ['in', 'is', 'a', 'and', 'are']

# Create inverted index ////
inverted_index = {}
for doc_id, doc_text in docs.items():
      # Remove stop words from the document text ////
      doc_text = re.sub(r'\b(' + '|'.join(stop_words) + r')\b\s*', '', doc_text)
      # Split the document text into words ////
      words = doc_text.split()
      # Add each word to the inverted index with its corresponding document ID ////
      for word in words:
            if word not in inverted_index:
                  inverted_index[word] = [doc_id]
            else:
                  inverted_index[word].append(doc_id)

# Get the postings list for a given term/word ////
term = input(' Enter a term/word: ')
if term in inverted_index:
      print(','.join(inverted_index[term]))
else:
      print(' This Term is not found in any document. ')