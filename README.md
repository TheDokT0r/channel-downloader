# channel-downloader
A simple script to download all videos from a YouTube channel.

## Installation
1. Install [Python 3](https://www.python.org/downloads/).
2. clone this repository:
```bash
https://github.com/TheDokT0r/channel-downloader.git
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
```bash
python src/Main.py <channel_id> <output_dir>
```

## Example
```bash
python src/Main.py UC-lHJZR3Gqxm24_Vd_AJ5Yw ./videos
```

You can also use the full channel URL (only if it contains the channel ID):
```bash
python src/Main.py https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw ./videos
```

## Plans for the future
- [] Add a GUI
- [] Add a progress bar
- [] Add a download speed indicator
- [] Create a Windows and Linux executable