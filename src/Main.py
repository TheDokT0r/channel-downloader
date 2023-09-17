from concurrent.futures import ThreadPoolExecutor
from GetAllVideosInChannel import get_all_video_in_channel
from GetChannelId import get_channel_id
from DownloadVideos import download_video
import sys

def main():
    channel_id = get_channel_id(sys.argv[1]) if len(sys.argv) > 1 else None
    out_dir = sys.argv[2] if len(sys.argv) > 2 else f"./{channel_id}/"

    if not channel_id:
        print("Invalid channel id or URL")
        return

    print(f"Getting all videos from channel: {channel_id}")
    all_video_links = get_all_video_in_channel(channel_id)

    with ThreadPoolExecutor() as executor:
        executor.map(download_video, all_video_links, [out_dir]*len(all_video_links))

    print("Finished downloading all videos")

if __name__ == "__main__":
    main()