# %%
import os
import pandas as pd


# %%
base_directory = os.path.join('..', '..')
HowTo100M_dir = os.path.join(base_directory, 'data', 'HowTo100M')
csv_fp = os.path.join(HowTo100M_dir, 'HowTo100M_v1.csv')
HowTo_df = pd.read_csv(csv_fp)

# %%
hl = 'en'
csv_filepath = os.path.join(HowTo100M_dir, f'video_titles-{hl}.csv')
video_titles = pd.read_csv(csv_filepath)

# %%
# there are probably more English languages supported on YouTube. But, in the HowTo100M dataset, there are only these.
ENGLISH_LANGUAGES = {'en', 'en-GB', 'en-US', 'en-CA', 'en-IN', 'en-IE'}
both_english = video_titles[(video_titles['defaultLanguage'].isin(ENGLISH_LANGUAGES)) & (video_titles['defaultAudioLanguage'].isin(ENGLISH_LANGUAGES))]

def isascii(row):
    return row['title'].isascii()

ascii_titles = both_english[both_english.apply(isascii, axis=1)]
