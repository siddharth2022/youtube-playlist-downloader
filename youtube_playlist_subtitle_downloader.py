from pytube import YouTube
import os, sys, time
import argparse
from urllib2 import urlopen

# write your url below


def get_playlist_links(playlist_url):
    page_elements = urlopen(playlist_url).readlines()
    video_elements = [el for el in page_elements if 'pl-video-title-link' in el]  # Filter out unnecessary lines
    video_urls = [v.split('href="',1)[1].split('" ',1)[0] for v in video_elements]  # Grab the video urls from the elements
    return ['http://www.youtube.com' + v for v in video_urls]    
    '''
    YouTube(url).streams.first().download()
    tube = YouTube(url)
    title = tube.title
    caption = tube.captions.get_by_language_code('en')
    if caption is not None:
                subtitle = caption.generate_srt_captions()
                file = open(title+".srt", "w")
                if file.writelines(subtitle) :
                     print "subtitle file has saved"
    '''

x = get_playlist_links("https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v")
print x
