# YouTube Titles and Transcripts Dataset

This repository contains code and meta-data to (re-)create the *YouTube Titles and Transcripts Dataset* as described in the following paper:

Christopher Lovejoy, William Davies, Demian Till and Louis Prosser. **The Truth Is In The Title? Video Title Generation as a novel training objective for video summarisation**. May 2021. ([link](https://chrislovejoy.me/video-title-prediction))


Please cite the following paper in all academic work that uses this dataset:

```
@inproceedings{lovejoy2021videotitle,
  title = {The Truth Is In The Title? Video Title Generation as a novel training objective for video summarisation},
  author = {Lovejoy, Davies, Till and Prosser},
  year = {2021},
}
```

We also acknowledge earlier work (including first-time data collection) on the same data (and encourage you to do the same):

* Shawn Hershey, Sourish Chaudhuri, Daniel P. W. Ellis, Jort F. Gemmeke, Aren Jansen, R. Channing Moore, Manoj Plakal, Devin Platt, Rif A. Saurous, Bryan Seybold, Malcolm Slaney, Ron J. Weiss, Kevin Wilson. CNN Architectures for Large-Scale Audio Classification. September 2016. [https://arxiv.org/abs/1609.09430v2](https://arxiv.org/abs/1609.09430v2)


## Download the Dataset

The full corpus consists of 1.2 million YouTube videos with transcripts and titles. Within this, there is a subset of 17,886 videos which meet the following criteria (i) YouTube metadata set to English language, (ii) human-generated summaries, with punctuation and (iii) titles only includes ASCII characters.

Both are available for download below.

<!-- TODO: add further description of the dataset; columns, etc -->


You can obtain the corpus in one of two ways:

### (Option 1): Download a pre-packaged version

#### 1. Puncutated English transcripts and titles (17,886 videos)

This contains 17,886 videos with punctuated English transcripts and titles. This is the dataset originally used in [paper title + link].

It can be downloaded [here](https://drive.google.com/uc?export=download&id=1iIdTK7mkzDmz7lYcZrcoEPpTIYYLTqoh).


#### 2. All videos transcripts and titles

This contains the full corpus of all 1.2 million YouTube videos with transcripts and titles. 

It can be downloaded [here](https://drive.google.com/uc?export=download&id=1K2fuVNHTK3IKQr3_I3Z0khQ-ss09WBYA).



### (Option 2): Use [this](https://github.com/chris-lovejoy/youtube-titles-and-transcripts/tree/main/reproduce#reproducible-pipeline-for-youtube-titles-and-transcripts) reproducible pipeline

<!-- TO DO: add link to subfolder README.md which walks through this -->



## Issues

If any issues, please raise them on this repository (https://github.com/chris-lovejoy/youtube-titles-and-transcripts/issues) or contact us [via email](mailto:snlpgroup0@gmail.com).


## License
At the time of release, all videos in the dataset have been made available by the original content creators under the standard [YouTube License](https://www.youtube.com/static?template=terms).

We are providing the contents of this repository under the [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Attribution-Share-Alike) License (for data-like content) and/ or [BSD-2-Clause License](https://opensource.org/licenses/BSD-2-Clause) (for software-type content).

