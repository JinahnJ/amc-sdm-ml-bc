# AMC bladder cancer transcriptomics classifier

This repository contains the code for classifying patient response to neoadjuvant chemotherapy in bladder cancer as either non-response (NR) or response (R). The classification is based on transcriptomics data from AMC (Asan Medical Center) datasets. The entire pipeline is built using Python (version 3.12).

## Installation

### Cloning and Setting Up Dependencies

To get started, clone the repository and set up the necessary directories:

<pre>
<code>
git clone https://github.com/JinahnJ/amc-sdm-ml-bc
cd amc-sdm-ml-bc
md dst
md src

</code>
</pre>

Create and activate the environment using Poetry:

<pre>
<code>
poetry shell
</code>
</pre>

### Running the code

Before running the code, ensure you have checked and properly edited the configuration file, typically located in the ./config directory.

You can run the classifier using:

<pre>
<code>
python mian.py -c CONFIG-PATH
</code>
</pre>

Alternatively, you can use the provided shell script:

<pre>
<code>
./run.sh
</code>
</pre>

The output will be saved by default in ./src/results.yaml.

### Citation

If you use this code in your research, please consider citing the following paper:

<pre>
<code>
@article{KIM2023101224,
title = {Glutathione dynamics is a potential predictive and therapeutic trait for neoadjuvant chemotherapy response in bladder cancer},
journal = {Cell Reports Medicine},
volume = {4},
number = {10},
pages = {101224},
year = {2023},
issn = {2666-3791},
doi = {https://doi.org/10.1016/j.xcrm.2023.101224},
url = {https://www.sciencedirect.com/science/article/pii/S2666379123003981},
author = {YongHwan Kim and Hyein Ju and Seung-Yeon Yoo and Jinahn Jeong and Jinbeom Heo and Seungun Lee and Ja-Min Park and Sun Young Yoon and Se Un Jeong and Jinyoung Lee and HongDuck Yun and Chae-Min Ryu and Jinah Lee and Yun Ji Nam and Hyungu Kwon and Jaekyoung Son and Gowun Jeong and Ji-Hye Oh and Chang Ohk Sung and Eui Man Jeong and Jaehoon An and Sungho Won and Bumsik Hong and Jae Lyun Lee and Yong Mee Cho and Dong-Myung Shin},
</code>
</pre>

This citation provides details about the predictive model and its biological relevance to bladder cancer treatment responses.

### Notes

- The dataset is available upon request by contacting the corresponding author of the following paper: https://doi.org/10.1016/j.xcrm.2023.101224
