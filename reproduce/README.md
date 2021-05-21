# Reproducible pipeline for YouTube-Titles-and-Transcripts

To create the full (1.2M) dataset, follow the instructions in the creating_dataset ipynb file.

To then also create two 'cleaner' subsets of this data, follow the instructions in the creating_clean_datasets ipynb file after having run the creating_dataset ipynb. The criteria used to create these subsets are:

#### 1. Titles only contain ASCII characters, defaultLanguage is English and defaultAudioLanguage is English (on YouTube). Dataset size is 74k. (Not provided as a direct download)

#### 2. Of these, only include videos with fully punctuated transcripts. Dataset size is 17,886.

## Overview

The procedure for reproducing these datasets is as follows:

### Full Dataset

* Download required files from https://www.di.ens.fr/willow/research/howto100m/. These are 'raw_caption.json', 'HowTo100M_v1.csv' and 'task_ids.csv'
* Download 'video_titles-en.csv' from [here](https://drive.google.com/uc?export=download&id=1LF7V0XmsM5A-f_CVkiwTUn78fAiB5LRd)
* Remove NaNs from HowTo100M dataset
* Map titles, categories, task_ids to YouTube video ID
* Concatenate captions from HowTo100M dataset into complete transcripts, handling newline characters and overlapping captions appropriately
* Create new csv containing columns for YouTube video ID, video title, video transcript, video categories and task ID (from HowTo100M dataset)
* Add punctuated flag
* Add additional columns for transcript length, defaultLanguage and defaultAudioLanguage (from YouTube)
* Remove transcripts over 42,500 characters long as these are junk transcripts

### Clean Datasets

* Download 'hlen_defaultLanguageEnglish_defaultAudioLanguageEnglish_ascii.csv' from [here](https://drive.google.com/uc?export=download&id=1tfaVHuYCxfgaeh2pWs4pKFUT_SRaS7Ob)
* Load full dataset
* Extract only videos with video IDs in the above csv to create 74k dataset
* Extract only videos from these with punctuated = 1 to create 18k dataset
