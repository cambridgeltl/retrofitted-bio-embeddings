# Retrofitted bio-embeddings

<PAPER NAME>.

Contact: Billy Chiu (billy1985322@gmail.com)

This repository contains the code and data for the retrofitting method presented in <PAPER NAME>. The word vectors which achieve the state of the art results can be downloaded <VECTOR LINK>.

Configuring the Tool
The tool reads all the experiment config parameters from the run_retrofit.sh file in the root directory.

The config file specifies:

WVDIR: the location of the initial word vectors (distributional_vectors);
LEXDIR: the sets of linguistic constraints to be injected into the vector space (synonyms_verb);
The config file also specifies the hyperparameters of the procedure (set to their default values in run_retrofit.sh).

The evaluation tasks can be downloaded from [here:Relation Extraction](https://github.com/jbjorne/TEES) and [here:Text classification](https://github.com/cambridgeltl/multilabel-nn).

Create retrofitted model
python ./run_retrofit.sh

Running the experiment loads the word vectors specified in the config file and fits them to the provided linguistic constraints. The procedure output the updated word vectors to the results directory as output_vec/final_vectors.bin (one word vector per line).

*Note that the vectors used in this experiment have been compressed from .txt format into .bin format, text2bin/bin2text tools are be download [here](https://github.com/marekrei/convertvec) 

Reference:
The paper which introduces the procedure:

 @inproceedings{
 }

If you are using bio-VerbNet constraints, please cite:
  @article{chiu2019neural,
    title={A neural classification method for supporting the creation of BioVerbNet},
    author={Chiu, Billy and Majewska, Olga and Pyysalo, Sampo and Wey, Laura and Stenius, Ulla and Korhonen, Anna and Palmer, Martha},
    journal={Journal of biomedical semantics},
    volume={10},
    number={1},
    pages={2},
    year={2019},
    publisher={BioMed Central}
  }
