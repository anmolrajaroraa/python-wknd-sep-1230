#pip install pytube
from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=ndl1W4ltcmg').streams.first().download()