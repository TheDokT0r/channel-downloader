import re

def get_channel_id(channel_url):
    # Extract the channel ID from the URL using a regular expression
    match = re.search(r'channel/([\w-]+)', channel_url)
    if match:
        return match.group(1)
    else:
        return None