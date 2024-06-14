### Serif Health Takehome - Matt Lewis

#### How to run the script 

Given that this is supposed to be a ~90 mins exercise, I tried to keep the script relatively simple. 
All imports are from the python standard library. 

With the assumption that you have python installed on a unix/mac machine: 



```
# install pyenv if you don't have it 
brew update
brew install pyenv

# install python 3.8 
pyenv install 3.8

# create an env and activate 
pyenv virtualenv 3.8 matt_takehome
pyenv activate matt_takehome

# run the script 
python takehome_script.py
# results written to locations.txt
```

#### Results
* 56 distinct URLs
* Runtime ~0:13:35

#### Discussion: 
* This script took around 90 mins to write, though there are clearly gains that could be made through refactoring. 
* Then general premise of this script was to iterate through the gzip file without fully loading it, parsing it bit by bit to extract relevant URLs through some basic text matching, and writing distinct url values to a text file. 
* The first task for this script was to find a way to stream through the gzipped file. A little searching showed me that we can do this pretty easily with `gzip`, part of the standard python library. I had to futz around somewhat to get this to work as needed. 
* If this was a task that was going to be repeated many times on the same/similar gzip file, there are some interesting things that could be done with some libraries that allow for random access of gzip files in Python, like [indexed_gzip](https://github.com/pauldmccarthy/indexed_gzip)
* > Anthem has an interactive MRF lookup system. This lookup can be used to gather additional information - but it requires you to input the EIN or name of an employer who offers an Anthem health plan: Anthem EIN lookup. How might you find a business likely to be in the Anthem NY PPO? How
can you use this tool to confirm if your answer is complete?
* Seems like you could use this tool to spot verify that the data we've parsed out of the file does indeed correspond to Anthem health plans through matching the EIN given in the gzip file.