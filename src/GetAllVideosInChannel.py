import scrapetube

def get_all_video_in_channel(channel_id):
    videos = scrapetube.get_channel(channel_id)

    # Map the videoId to a full YouTube URL
    videos = [f'https://www.youtube.com/watch?v={video["videoId"]}' for video in videos]
    return videos