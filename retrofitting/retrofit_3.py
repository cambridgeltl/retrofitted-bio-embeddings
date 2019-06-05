import argparse
import gzip
import math
import numpy, sys
import re, os
import sys, codecs
import collections
from copy import deepcopy
from gensim.models.keyedvectors import KeyedVectors


isNumber = re.compile(r'\d+.*')
def norm_word(word):
  #if isNumber.search(word.lower()):
  if isNumber.search(word):
    return '---num---'
  elif re.sub(r'\W+', '', word) == '':
    return '---punc---'
  else:
    #return word.lower()
    return word.strip()

def readWordVectors(filename, bin=True):
    sys.stderr.write('Reading vectors from file...\n')

    model = KeyedVectors.load_word2vec_format(filename, unicode_errors='ignore', binary=bin)

    
    vectorDim = model.syn0.shape[1]
    print ("vectorDim:", model.syn0.shape, '\n')

    wordVectors = model
    sys.stderr.write('Loaded vectors from file...\n')

    vocab = {word: model.vocab[word].index for word in model.vocab}

    sys.stderr.write('Finished reading vectors.\n')

    return vocab, wordVectors, vectorDim

# Write word vectors to file
def print_word_vectors(wordVectors, vectorDim, filename, bin=True):
    sys.stderr.write('Writing vectors to file...\n')
    print ('Word in output vec...', len(wordVectors.vocab), '\n')

    wordVectors.save_word2vec_format(filename, binary=bin)

    sys.stderr.write('Finished writing vectors.\n')

def write_dict(word_vectors, write_path):
    """
    This function prints the collection of word vectors to file, in a plain textual format. 
    """
 
    f_write = codecs.open(write_path, 'w', 'utf-8') 
    dimens = len(word_vectors.values()[0])
    total_line = 0
    for i, key in enumerate(word_vectors):
        try:
            if key.strip() != "" and len(word_vectors[key]) == dimens:
                w = key.encode('utf-8')
                total_line +=1
                #print >>f_write, key, " ".join(map(unicode, numpy.round(word_vectors[key], decimals=6)))
        except UnicodeDecodeError:
            continue
 
    # # write w2v heading
    print >>f_write, total_line, dimens
    for i, key in enumerate(word_vectors):
        try:
            if key.strip() != "" and len(word_vectors[key]) == dimens:
                print >>f_write, key, " ".join(map(unicode, numpy.round(word_vectors[key], decimals=6)))
        except UnicodeDecodeError:
            continue
     
    print ("total_line", total_line)
    print ("Original_Vector len:", len(word_vectors), 'Printed:',total_line, "word vectors to:", write_path)
    

''' Read the lexicon word relations as a dictionary '''
def read_lexicon(filename):
  # updated: to retrofit memeber verbs in class as well
  lexicon = {}
  for line in open(filename, 'r'):
    words = line.lower().strip().split()
    for ii, w in enumerate(words):
      lexicon[w] = [norm_word(word) for jj, word in enumerate(words) if jj!=ii]
  return lexicon

def update(wordVectors, rf_Vectors, word):
  #numpy.put(wordVectors[word], range(len(rf_Vectors)), rf_Vectors)
  wordVectors[word] = rf_Vectors
  return wordVectors

''' Retrofit word vectors to a lexicon '''
def retrofit(wordVecs, lexicon, numIters, thr):
  sys.stderr.write('Starting the retrofitting procedure...\n')
  newWordVecs = deepcopy(wordVecs)

  wvVocab = set(wordVecs.vocab)
  print ("Words in input: ", len(wordVecs.vocab))
  
  loopVocab = wvVocab.intersection(set(lexicon.keys()))
  for it in range(numIters):
    # loop through every node also in ontology (else just use data estimate)
    for word in loopVocab:
      wordNeighbours = set(lexicon[word]).intersection(wvVocab)
      numNeighbours = len(wordNeighbours)

      #no neighbours, pass - use data estimate
      if numNeighbours == 0:
        continue
      
      newVec = numNeighbours * newWordVecs[word]

      # loop over neighbours and add to new vector (currently with weight 1)
      for ppWord in wordNeighbours:
        # the weight of the data estimate if the number of neighbours
        newVec += thr * newWordVecs[ppWord]
        
      newWordVecs = update(newWordVecs, newVec/(2*numNeighbours), word)

  return newWordVecs


if __name__=='__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", type=str, default=None, help="Input word vecs")
  parser.add_argument("-l", "--lexicon", type=str, default=None, help="Lexicon file name")
  parser.add_argument("-o", "--output", type=str, help="Output word vecs")
  parser.add_argument("-n", "--numiter", type=int, default=10, help="Num iterations")
  parser.add_argument("-t", "--thr", type=float, default=0.05, help="learning_rate")
  args = parser.parse_args()

  vocab, wordVecs, vectorDim = readWordVectors(args.input)
  sys.stderr.write('vocab length is '+str(len(vocab.keys()))+'\n')

  lexicon = read_lexicon(args.lexicon)
  numIter = int(args.numiter)
  outFileName = args.output
  thr = float(args.thr)
  
  ''' Enrich the word vectors using ppdb and print the enriched vectors '''
  newWordVecs = retrofit(wordVecs, lexicon, numIter, thr)
  print_word_vectors(newWordVecs, vectorDim, outFileName)