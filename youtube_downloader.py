from pytube import YouTube

# Ask the user for the video URL
url = input("Enter your URL > ")

# Create a YouTube video object
video = YouTube(url)

# Get the video with the highest resolution
downloader = video.streams.get_highest_resolution()

# Download the video
downloader.download()
