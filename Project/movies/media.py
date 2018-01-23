#-*- coding:utf-8 -*-
import webbrowser

class Movie():
	'''This is the class of movie, which one contains movie info, and also can operate movie, like open it'''

    def __init__(self,title,line,poster,url):
        self.title = title
        self.line = line
        self.poster_image_url = poster
        self.trailer_youtube_url = url
    def showTrailer(self):
        webbrowser.open(self.url)















