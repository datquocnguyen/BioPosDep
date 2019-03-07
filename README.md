
# Biomedical POS tagging and dependency parsing models

Biomedical POS tagging and dependency parsing models are trained on  [GENIA](http://www.geniaproject.org/) and [CRAFT](http://BioPosDep-corpora.sourceforge.net/CRAFT/). See [our following paper](https://arxiv.org/abs/1808.03731) for more details:

	@Article{NguyenK2019,
	author="Nguyen, Dat Quoc and Verspoor, Karin",
	title="From POS tagging to dependency parsing for biomedical event extraction",
	journal="BMC Bioinformatics",
	year="2019",
	month="Feb",
	day="12",
	volume="20",
	number="1",
	pages="72",
	doi="10.1186/s12859-019-2604-0",
	url="https://doi.org/10.1186/s12859-019-2604-0"
	}
    
Our models are **free** for non-commercial use and distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International ([CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)) License. 

<img width="400" alt="pos" src="https://user-images.githubusercontent.com/2412555/53179172-c9de7500-3625-11e9-90ac-17fe3ca016b0.png"> <img width="400" alt="dep" src="https://user-images.githubusercontent.com/2412555/53179163-c6e38480-3625-11e9-954d-9676730e7b27.png">

# Usage 

#### The first step is to perform POS tagging and dependency parsing using [NLP4J](https://emorynlp.github.io/nlp4j/) models. Here, NLP4J would also perform _TOKENIZATION_ and _SENTENCE SEGMENTATION_ if input files are raw text corpora. Then, the output of NLP4J will be used as input for other dependency parsing models.

### Perform biomedical POS tagging and dependency parsing using retrained NLP4J models 

#### Installation

Download NLP4J models from [https://github.com/datquocnguyen/BioPosDep/archive/master.zip](https://github.com/datquocnguyen/BioPosDep/archive/master.zip) (70MB) or clone these models using `git`:
    
    $ git clone https://github.com/datquocnguyen/BioPosDep.git
    
To run the models, it is expected that `Java` is already set to run in command line or terminal.

#### Command line 
    
    # Using models trained on GENIA
    BioPosDep/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i <filepath> -format <string> [-ie <string> -oe <string>]
    
    # Using models trained on CRAFT
    BioPosDep/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i <filepath> -format <string> [-ie <string> -oe <string>]
	
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
	BioPosDep/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/raw.txt -format raw -oe genia
	BioPosDep/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/raw.txt -format raw -oe craft
	
	# For a sentence-segmented corpus input (without tokenization!)
	BioPosDep/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/sentence_segmented.txt -format line -oe genia
	BioPosDep/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/sentence_segmented.txt -format line -oe craft

	# For a "pre-processed" tokenized and sentence-segmented corpus
		# Convert into a column-based format
	BioPosDep/NLP4J$ python ../get_ColumnFormat.py ../data/tokenized_sentence_segmented.txt
		# Apply models using "tsv". Here we expect word forms at the second column (i.e. column index of 1). 
		# Adjust <column index="1" field="form"/> in config-GENIA.xml and config-CRAFT.xml if users already have a column-formated corpus with a different index of the word form column.
	BioPosDep/NLP4J$ bin/nlpdecode -c config-GENIA.xml -i ../data/tokenized_sentence_segmented.txt.column -format tsv -oe genia
	BioPosDep/NLP4J$ bin/nlpdecode -c config-CRAFT.xml -i ../data/tokenized_sentence_segmented.txt.column -format tsv -oe craft
	

From the examples above, output files `.genia` and `.craft ` are generated in folder `data`, containing POS and dependency annotations.  


#### NOTE
Those NLP4J output files are in a 9-column format. To further apply other dependency parsing models, they must be converted to 10-column format:

	# Command line
	BioPosDep$ python convert_NLP4J_to_CoNLL.py <NLP4J_output_filepath>

	# Examples
	BioPosDep$ python convert_NLP4J_to_CoNLL.py data/raw.txt.genia
	BioPosDep$ python convert_NLP4J_to_CoNLL.py data/raw.txt.craft

##### Two 10-column output files `raw.txt.genia.conll` and `raw.txt.craft.conll` are generated in folder `data`, which will be used as inputs for other models.
	
### Using retrained Stanford [Biaffine](https://github.com/tdozat/Parser-v2) parsing models 

#### Installation

	# Install prerequisite packages  
	BioPosDep/StanfordBiaffineParser-v2$ virtualenv .TF1_0
	BioPosDep/StanfordBiaffineParser-v2$ source .TF1_0/bin/activate
	BioPosDep/StanfordBiaffineParser-v2$ pip install tensorflow==1.0
	BioPosDep/StanfordBiaffineParser-v2$ pip install numpy==1.11.0
	BioPosDep/StanfordBiaffineParser-v2$ pip install scipy==1.0.0
	BioPosDep/StanfordBiaffineParser-v2$ pip install matplotlib==2.1.2
	BioPosDep/StanfordBiaffineParser-v2$ pip install backports.lzma

 - Download file `Pre-trained-Biaffine-v2.zip` from [HERE](https://drive.google.com/file/d/18IYSJEV0uwbg468lFXejS0Wyw2_8Pjfa/view?usp=sharing). 
 - Unzip the file, then copy/move folder `models` and file `PubMed-shuffle-win2-500Kwords.txt` into folder `BioPosDep/StanfordBiaffineParser-v2`.



#### Command line 

	# Using model trained on GENIA
	BioPosDep/StanfordBiaffineParser-v2$ python main.py --save_dir models/GENIA parse <input_file_path>
	
	# Using model trained on CRAFT
	BioPosDep/StanfordBiaffineParser-v2$ python main.py --save_dir models/CRAFT parse <input_file_path>

	# Output parsed files are by default saved in the model directory with the same name as the input file.
	# NOTE: We can also specify the output directory with the --output_dir flag and/or the output file name with the --output_file flag.

#### Examples

	# Activate TensorFlow 1.0 before running models:
	BioPosDep/StanfordBiaffineParser-v2$ source .TF1_0/bin/activate
	BioPosDep/StanfordBiaffineParser-v2$ python main.py --save_dir models/GENIA parse ../data/raw.txt.genia.conll
	BioPosDep/StanfordBiaffineParser-v2$ python main.py --save_dir models/CRAFT parse ../data/raw.txt.craft.conll
	
Two output  parsed files `raw.txt.genia.conll` and `raw.txt.craft.conll` are generated in folders  `models/GENIA` and `models/CRAFT`, respectively.
	
### Using retrained jPTDP models 

See [https://github.com/datquocnguyen/jPTDP](https://github.com/datquocnguyen/jPTDP) for details. 
