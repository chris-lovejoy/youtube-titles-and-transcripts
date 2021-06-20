# %%
import os
import pandas as pd


# %%
base_directory = os.path.join('..')
HowTo100M_dir = os.path.join(base_directory, 'data', 'HowTo100M')
csv_fp = os.path.join(HowTo100M_dir, 'HowTo100M_v1.csv')
HowTo_df = pd.read_csv(csv_fp)

# %%
hl = 'en'  # hl parameter of YouTube API Videos: list call
csv_filepath = os.path.join(HowTo100M_dir, f'video_titles-{hl}.csv')
all_video_titles = pd.read_csv(csv_filepath)  # titles of all HowTo100M videos

# %%
# there are probably more English languages supported on YouTube. But, in the HowTo100M dataset, there are only these.
ENGLISH_LANGUAGES = {'en', 'en-GB', 'en-US', 'en-CA', 'en-IN', 'en-IE'}
# filter by YouTube metadata and all ASCII title
both_english = all_video_titles[(all_video_titles['defaultLanguage'].isin(ENGLISH_LANGUAGES)) & (all_video_titles['defaultAudioLanguage'].isin(ENGLISH_LANGUAGES))]

def isascii(row):
    return row['title'].isascii()

clean_titles = both_english[both_english.apply(isascii, axis=1)]
clean_titles.to_csv(os.path.join(HowTo100M_dir, f'clean_video_titles-{hl}.csv'), index=False)
