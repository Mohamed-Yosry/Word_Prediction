# imports
import string
import nltk
nltk.download('punkt')
nltk.download('ngrams')
nltk.download('gutenberg')
from nltk.corpus import gutenberg
from nltk import FreqDist
from nltk.util import ngrams
from collections import defaultdict
from operator import itemgetter

# input the reuters sentences
sents = gutenberg.words('melville-moby_dick.txt')

# write the removal characters
removal_list = list(string.punctuation)

#making word lowercase letters
tokens = [word.lower() for word in sents]

#remove from tokens removalble words
new_tokens = []
for word in tokens:
  if word not in removal_list:
    new_tokens.append(word)

#creating token set for removing dublicated words
tokens_set = set(new_tokens)

#generating trigram & bigram
trigram = nltk.trigrams(new_tokens)
bigram = nltk.bigrams(new_tokens)

#frequency of trigram & bigram
freq_tri = nltk.FreqDist(trigram)
freq_bi = nltk.FreqDist(bigram)

# for tok in freq_tri.keys():
#   print(tok,freq_tri[tok])
# print("----------------------------------------------------------------------------------------") 

print(freq_tri[('he','was','a')])
print(freq_bi[('he','was')])

#suggest next word
def suggest_next(input,trigram_freq,bigram_freq):
  input.lower()
  input = nltk.word_tokenize(input)

  #stroing word and it's probalbility
  words_prob = []
  trigram_count = 0
  bigram_count = 0
  for word in tokens_set:
    trigram_count = freq_tri[(input[-2],input[-1],word)]
    bigram_count = freq_bi[(input[-2],input[-1])]
    if bigram_count>0.0:
      probability = trigram_count / bigram_count
      words_prob.append([word,probability])
    # if(probability > 0.0):
    #   words_prob.append([word,probability])
    
  #sorting list of lists based on probability of index(1) of inner lists
  words_prob = sorted(words_prob, key=itemgetter(1))
  return words_prob

#calling suggest_next in infinity loop taking inputs and printing the result
while 0!=1:
  user_input = input("Enter your string: ")
  result=suggest_next(user_input,freq_tri,freq_bi)
  if len(result) < 5:
    print(result)
  else:
    print(result[-5:])
  print("-------------------------------------------------------------------")