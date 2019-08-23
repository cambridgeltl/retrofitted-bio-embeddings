# Retrofitted bio-embeddings

## Enhancing biomedical word embeddings by retrofitting to verb clusters

Contact: Billy Chiu (billy1985322@gmail.com)

This repository contains the code and retrofitted embeddings for the paper *[Enhancing biomedical word embeddings by retrofitting to verb clusters](https://www.aclweb.org/anthology/W19-5014)* in BioNLP 2019. 

The following word embeddings files (.bin format) achieve the state-of-the-art (SOTA) results, they can be downloaded from here (1.68 GB each file): 

* [Word embeddings retrofitted to 16 verb classes ](https://ndownloader.figshare.com/files/17414963)

* [Word embeddings retrofitted to 34 verb classes](https://ndownloader.figshare.com/files/17414960) (this achieved SOTA on relation extraction & sentence classification)

* [Word embeddings retrofitted to 50 verb classes](https://ndownloader.figshare.com/files/17414957) (this achieved SOTA on document classification)

You can download there files from [here](https://figshare.com/articles/Enhancing_biomedical_word_embeddings_by_retrofitting_to_verb_clusters/9723827).

**Note that these embeddings have been compressed from .txt format into .bin format using *text2bin/bin2text* tools are be download [here](https://github.com/marekrei/convertvec) 

### Configuring the Tool
The tool reads all the experiment config parameters from the run_retrofit.sh file in the root directory.

The config file specifies:

WVDIR: the location of the initial word vectors (distributional_vectors);
LEXDIR: the sets of linguistic constraints to be injected into the vector space (synonyms_verb);
The config file also specifies the hyperparameters of the procedure (set to their default values in run_retrofit.sh).

The evaluation tasks can be downloaded from [Relation Extraction](https://github.com/jbjorne/TEES) and [Text classification](https://github.com/cambridgeltl/multilabel-nn).

### Create retrofitted model
python ./run_retrofit.sh

Running the experiment loads the word vectors specified in the config file and fits them to the provided linguistic constraints. The procedure output the updated word vectors to the results directory as output_vec/final_vectors.bin (one word vector per line).


### Reference
please cite our paper:
 ```
@inproceedings{chiu2019enhancing,
  title={Enhancing biomedical word embeddings by retrofitting to verb clusters},
  author={Chiu, Billy and Baker, Simon and Palmer, Martha and Korhonen, Anna},
  booktitle={Proceedings of the 18th BioNLP Workshop and Shared Task},
  pages={125--134},
  year={2019}
}
 ```
