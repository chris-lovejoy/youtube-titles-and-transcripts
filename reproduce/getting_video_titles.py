# %%
# !
# %%
import os
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

# %%
try:
    from google.colab import drive
    drive.mount('/content/drive')
    base_directory = '/content/drive/My Drive/'
except ModuleNotFoundError:
    base_directory = '..'

# %%
def get_response(youtube, video_ids, hl):
    # can only request 50 ids at a time: https://stackoverflow.com/questions/36370821/does-youtube-v3-data-api-have-a-limit-to-the-number-of-ids-you-can-send-to-vide
    assert len(video_ids) <= 50
    ids_as_string = ','.join(id for id in video_ids)
    
    request = youtube.videos().list(
        part="snippet",
        id=ids_as_string,
        hl=hl
    )
    response = request.execute()
    return response


# %%
api_service_name = "youtube"
api_version = "v3"
with open('key.txt', 'r') as f:
    key = f.read()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=key)

# %%
class VideoInformationGetter:
    """
    Requests information about video (using video_id) from YouTube API.
    Builds mapping from id to video information.
    """
    def __init__(self, video_ids, csv_filepath, stop, hl, youtube, print_every=1e5, filter_api_response=lambda video: video['snippet']['localized']['title']):
        """

        Args:
            video_ids: YouTube video ids for which you want to scrape video information.
            csv_filepath: the filepath at which you want to save the video information.
            stop: you want to scrape video information until the {{stop}}'th video in video_ids.
            hl: localization parameter for YouTube API call
            youtube: YouTube API instance
            print_every:
            filter_api_response: mapping from YouTube API response to dictionary of information that you want to save for each video
            id.
        """
        self.video_ids = video_ids
        self.csv_filepath = csv_filepath
        self.parse_single_video_resource = filter_api_response
        self.stop = stop
        self.hl = hl
        self.print_every = print_every
        self.youtube = youtube

    def get_start_idx(self):
        try:
            last_id_that_has_been_titled = self._get_last_id_that_has_been_titled()
        except FileNotFoundError:
            return 0

        idx_of_last_idx_that_has_been_titled = (self.video_ids == last_id_that_has_been_titled).nonzero()[0].item()
        return idx_of_last_idx_that_has_been_titled + 1  # +1 because we want to start scraping from the NEXT id

    def _get_last_id_that_has_been_titled(self):
        return self.current_video_information['id'].iloc[-1]

    @property
    def current_video_information(self):
        return pd.read_csv(self.csv_filepath)

    def parse_api_response(self, response):
        """

        Args:
            response: dict: response from YouTube API v3 with argument part="snippet"

        Returns:
            relevant_information_about_videos: dict: maps from video attribute (e.g. id, title) to a list of values. the list
            contains the values for all the videos in `response`.
        """
        assert response['kind'] == "youtube#videoListResponse"

        video_resources = response['items']
        relevant_information_about_videos = self.parse_single_video_resource(video_resources[0])
        # initialize list
        for key, val in relevant_information_about_videos.items():
            relevant_information_about_videos[key] = [val]

        for video_resource in video_resources[1:]:
            single_video_information = self.parse_single_video_resource(video_resource)
            for key, val in single_video_information.items():
                relevant_information_about_videos[key] = relevant_information_about_videos[key] + [val]
        return relevant_information_about_videos

    def save_new_videos(self, new_video_information):
        new_video_df = pd.DataFrame.from_dict(new_video_information)
        if not os.path.isfile(self.csv_filepath):
            new_video_df.to_csv(self.csv_filepath, mode='a', index=False, header=True)
        else:
            new_video_df.to_csv(self.csv_filepath, mode='a', index=False, header=False)

    def build_database(self):
        MAX_IDS_PER_REQUEST = 50

        start = self.get_start_idx()
        print(f'start: {start}')
        print_counter = 0
        for start_idx in range(start, self.stop, MAX_IDS_PER_REQUEST):
            ids = self.video_ids[start_idx: start_idx + MAX_IDS_PER_REQUEST]
            response = get_response(youtube=self.youtube, video_ids=ids, hl=self.hl)
            relevant_information_about_videos = self.parse_api_response(response)
            self.save_new_videos(relevant_information_about_videos)

            print_counter += MAX_IDS_PER_REQUEST
            if print_counter % self.print_every == 0:
                print(f'start_idx: {start_idx}')


# %%
def parse_api_response(video):
    title = video['snippet']['title']
    localized_title = video['snippet']['localized']['title']
    defaultLanguage = video['snippet'].get('defaultLanguage', 'NONE')
    defaultAudioLanguage = video['snippet'].get('defaultAudioLanguage', 'NONE')
    id = video['id']

    info = {'id': id,
            'title': title,
            'localized_title': localized_title,
            'defaultLanguage': defaultLanguage,
            'defaultAudioLanguage': defaultAudioLanguage
            }

    return info


# %%
HowTo100M_dir = os.path.join(base_directory, 'data', 'HowTo100M')
csv_fp = os.path.join(HowTo100M_dir, 'HowTo100M_v1.csv')
HowTo_df = pd.read_csv(csv_fp)
video_ids = HowTo_df['video_id'].values
stop = 400


# %%
hl = 'en'
video_info_getter = VideoInformationGetter(video_ids=video_ids,
                                           csv_filepath=os.path.join(HowTo100M_dir, f'video_titles-{hl}.csv'),
                                           filter_api_response=parse_api_response,
                                           stop=stop,
                                           hl=hl,
                                           youtube=youtube,
                                           print_every=5e4)

video_info_getter.build_database()
