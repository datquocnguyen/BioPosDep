
# Pre-trained models for biomedical POS tagging and dependency parsing

Pre-trained models for biomedical POS tagging and dependency parsing are trained on  [GENIA](http://www.geniaproject.org/) and [CRAFT](http://bionlp-corpora.sourceforge.net/CRAFT/). See our following paper for more details:

    @article{NguyenVerspoor2018bionlp,
        title = {{From POS tagging to dependency parsing for biomedical event extraction}},
        author = {Dat Quoc Nguyen and Karin Verspoor},
        journal = {arXiv preprint arXiv:1808.03731},
        year = {2018},
        url = {https://arxiv.org/abs/1808.03731}
    }
    
The pre-trained models are **free** for non-commercial use and distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International ([CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)) License. 

# Usage 

The first step is to perform POS tagging and dependency parsing using pre-trained [NLP4J](https://emorynlp.github.io/nlp4j/) models. Then other pre-trained dependency parsing models might be applied on top of the output of [NLP4J](https://emorynlp.github.io/nlp4j/). 

### Perform biomedical POS tagging and dependency parsing using pre-trained NLP4J models 

#### Installation

Users can download pre-trained NLP4J models from [https://github.com/datquocnguyen/BioNLP/archive/master.zip](https://github.com/datquocnguyen/BioNLP/archive/master.zip) (70MB) or clone these models using `git`:
    
    $ git clone https://github.com/datquocnguyen/BioNLP.git
    
To run the models, it is expected that `Java` is already set to run in command line or terminal.

#### Command line 
    
    # Using models trained on GENIA
    BioNLP/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i <filepath> -format <string> [-ie <string> -oe <string>]
    
    # Using models trained on CRAFT
    BioNLP/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i <filepath> -format <string> [-ie <string> -oe <string>]
	
	-i       <filepath> : input path (required)
	-format  <string>   : format of the input data (raw|line|tsv; default: raw)
	-ie      <string>   : input file extension (default: *)
	-oe      <string>   : output file extension (default: nlp)

 - `-i`  specifies the input path pointing to either a file or a directory. When the path points to a file, only the specific file is processed. When the path points to a directory, all files with the file extension  `-ie`  under the specific directory are processed.
 - `-format` specifies the format of the input file: `raw`, `line`, or `tsv`
	 - `raw`  accepts texts in any format
	 - `line`  expects a sentence per line
	 - `tsv`  expects columns delimited by `\t` and sentences separated by `\n`
 - `-ie`  specifies the input file extension. The default value  `*`  implies files with any extension. This option is used only when the input path  `-i`  points to a directory.
 - `-oe`  specifies the output file extension appended to each input filename. The corresponding output file, consisting of the NLP output, will be generated.

#### Examples
	
	# For a raw corpus input
	BioNLP/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/raw.txt -format raw -oe genia
	BioNLP/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/raw.txt -format raw -oe craft
	
	# For a sentence-segmented corpus input (without tokenization!)
	BioNLP/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/sentence_segmented.txt -format line -oe genia
	BioNLP/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/sentence_segmented.txt -format line -oe craft

	# For a "pre-processed" tokenized and sentence-segmented corpus
	BioNLP/NLP4J$ python ../get_ColumnFormat.py ../data/tokenized_sentence_segmented.txt
	BioNLP/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/tokenized_sentence_segmented.txt.column -format tsv -oe genia
	BioNLP/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/tokenized_sentence_segmented.txt.column -format tsv -oe craft
	# Here we expect word forms at the second column (i.e. column index of 1). 
	# Adjust <column index="1" field="form"/> in config-GENIA.xml and config-CRAFT.xml if users already have a column-formated corpus with a different index of the word form column.

From the examples above, output files `.genia` and `.craft ` are generated in folder `data`, containing POS and dependency annotations.  Note that these output files are in a 9-column format. To further apply other pre-trained dependency parsing models, they must be converted to 10-column format:

	BioNLP$ python convert_NLP4J_to_CoNLL.py <NLP4J_output_filepath>

##### Examples
	
	BioNLP$ python convert_NLP4J_to_CoNLL.py data/raw.txt.genia
	BioNLP$ python convert_NLP4J_to_CoNLL.py data/raw.txt.craft

will generate two 10-column output files `raw.txt.genia.conll` and `raw.txt.craft.conll` in folder `data`.
	
### Using pre-trained Stanford Biaffine models 
More documentation to come!

# References
	
	% NLP4J POS tagger
	@InProceedings{choi:2016:N16-1,
	  author    = {Choi, Jinho D.},
	  title     = {Dynamic Feature Induction: The Last Gist to the State-of-the-Art},
	  booktitle = {Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
	  month     = {June},
	  year      = {2016},
	  address   = {San Diego, California},
	  publisher = {Association for Computational Linguistics},
	  pages     = {271--281},
	  url       = {http://www.aclweb.org/anthology/N16-1031}
	}
	
	% NLP4J dependency parser
	@InProceedings{choi-mccallum:2013:ACL2013,
	  author    = {Choi, Jinho D.  and  McCallum, Andrew},
	  title     = {Transition-based Dependency Parsing with Selectional Branching},
	  booktitle = {Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
	  month     = {August},
	  year      = {2013},
	  address   = {Sofia, Bulgaria},
	  publisher = {Association for Computational Linguistics},
	  pages     = {1052--1062},
	  url       = {http://www.aclweb.org/anthology/P13-1104}
	}
	
	% For Biaffine 
	@InProceedings{dozat-qi-manning:2017:K17-3,
	  author    = {Dozat, Timothy  and  Qi, Peng  and  Manning, Christopher D.},
	  title     = {Stanford's Graph-based Neural Dependency Parser at the CoNLL 2017 Shared Task},
	  booktitle = {Proceedings of the CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies},
	  month     = {August},
	  year      = {2017},
	  address   = {Vancouver, Canada},
	  publisher = {Association for Computational Linguistics},
	  pages     = {20--30},
	  url       = {http://www.aclweb.org/anthology/K17-3002}
	}
	
	% For jPTDP
	@InProceedings{nguyen-dras-johnson:2017:K17-3,
	  author    = {Nguyen, Dat Quoc  and  Dras, Mark  and  Johnson, Mark},
	  title     = {A Novel Neural Network Model for Joint POS Tagging and Graph-based Dependency Parsing},
	  booktitle = {Proceedings of the CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies},
	  month     = {August},
	  year      = {2017},
	  address   = {Vancouver, Canada},
	  publisher = {Association for Computational Linguistics},
	  pages     = {134--142},
	  url       = {http://www.aclweb.org/anthology/K17-3014}
	}