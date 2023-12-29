from pytube import YouTube
import time


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path='./resources')
    except:
        print("An error has occurred")


if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    Download(link)
