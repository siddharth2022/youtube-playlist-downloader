from pytube import YouTube
# write your url below
url="https://www.youtube.com/watch?v=SSu00IRRraY"

YouTube(url).streams.first().download()
tube = YouTube(url)
title = tube.title
caption = tube.captions.get_by_language_code('en')
if caption is not None:
            subtitle = caption.generate_srt_captions()
            file = open(title+".srt", "w")
            if file.writelines(subtitle) :
                 print "subtitle file has saved"
            
            
