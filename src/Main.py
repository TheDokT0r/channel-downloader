from GetAllVideosInChannel import get_all_video_in_channel
from GetChannelId import get_channel_id
import sys

def main():
    channel_id = sys.argv[1]

    if channel_id.startswith("http") or channel_id.startswith("www") or channel_id.startswith("youtube"):
        try:
            channel_id = get_channel_id(channel_id)
        except:
            print("Invalid channel URL")
            return

    print(f"Getting all videos from channel: {channel_id}")
    all_video_links = get_all_video_in_channel(channel_id)
    for video in all_video_links:
        print(video)

if __name__ == "__main__":
    main()