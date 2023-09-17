from pytube import YouTube

def download_video(video_url, out_dir):
    print(f"Downloading video: {video_url}")
    yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(out_dir)
    print(f"Finished downloading video: {video_url}")