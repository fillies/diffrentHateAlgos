# Hate Speech Classifier Evaluation Project

## Overview

This Git project focuses on testing different hate speech classifiers for multiple languages, including German, English, and Multilingual. The classifiers are provided through Hugging Face and include models from various sources. The project takes a simple CSV file with a "text" column as input and outputs separate CSV files for each classifier. Classifier as set to be bianry hate no hate at the moment.

## Classifiers and URLs

1. [Google Jigsaw Classifier](https://jigsaw.google.com/) - **Note:** An API key is required for this classifier.

2. [IMSyPP Hate Speech Classifier (English)](https://huggingface.co/IMSyPP/hate_speech_en)

3. [Hatexplain BERT Classifier](https://huggingface.co/Hate-speech-CNERG/bert-base-uncased-hatexplain)

4. [RoBERTa Hate Speech Classifier (Facebook)](https://huggingface.co/facebook/roberta-hate-speech-dynabench-r4-target)

5. [XLM-Roberta Large Hate Speech Classifier (Multilingual)](https://huggingface.co/christinacdl/xlm_Roberta_Large_hate_speech_multilingual_binary)

6. [Multilingual Hate Speech Classifier (Robacofi)](https://huggingface.co/Andrazp/multilingual-hate-speech-robacofi)

## Input and Output

- **Input:** The project accepts a simple CSV file with a column named "text" containing the text data to be classified.

- **Output:** Separate CSV files are generated for each classifier, containing the original text along with the classification results.

# Contribution
Contributions are welcome!

# License
tbd
