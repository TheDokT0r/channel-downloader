import re

def get_channel_id(channel_url):
    if not channel_url:
        return None
    
    if channel_url.startswith("https://www.youtube.com/channel/"):
        return channel_url.split("/")[-1]

    if not channel_url.startswith("https") or not channel_url.startswith("http") or not channel_url.startswith("www") or not channel_url.startswith("youtube"):
        return channel_url

    # Extract the channel ID from the URL using a regular expression
    match = re.search(r'channel/([\w-]+)', channel_url)
    if match:
        return match.group(1)
    else:
        return None