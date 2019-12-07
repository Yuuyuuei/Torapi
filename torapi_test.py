# -*- coding: utf-8 -*-
from Torapi import Torapi
from Torapi.Filters import *
import time

# !! IMPORTANT: Notice the time.sleep(1) before each Get() request

t = Torapi()

# Everything is returned in JSON

# Returning a simple list
time.sleep(1)
t.Get()

time.sleep(1)
t.List().Get()

# Searches
# Simple Torrent search
time.sleep(1)
t.Search('torrent name').Get()

time.sleep(1)
t.SearchIMDB("tt123456").Get() # Searches movie id from http://www.imdb.com/

time.sleep(1)
t.SearchTVDB("123456").Get() # Searches http://thetvdb.com/

time.sleep(1)
t.SearchTheMovieDB("123456").Get() # Searches https://www.themoviedb.org/

# Filtering searches and list

# By category
time.sleep(1)
t.List().Category(Category.ALL).Get() # Returns list of torrents from a category (More categories below)

time.sleep(1)
t.Search('torrent name').Category(Category.ALL).Get()

# Limit
# 25, 50 or 100
time.sleep(1)
t.List().Limit(25).Get() 

# Sorting
# Seeders, leechers or last
time.sleep(1)
t.List().Sort(Sort.LAST).Get()

# Minimum seeders/leechers
time.sleep(1)
t.List().MinSeeders(10).Get()

time.sleep(1)
t.List().MinLeechers(10).Get()

# Extended JSON information
time.sleep(1)
t.List().Extended(True).Get() # Returns a list of torrents with extended information

# Ranked torrents
# Information from https://torrentapi.org/apidocs_v2.txt
# By default the api will return only ranked torrents ( internal ) , scene releases + -rarbg releases + -rartv releases.
# If you want other groups included in the results use the ranked parameter with a value of 0 to get them included.
time.sleep(1)
t.List().Ranked(False).Get()

# All methods can be mixed together in any order
time.sleep(1)
t.List().Limit(25).Sort(Sort.LAST).Ranked(False).Extended(True).Get()

# Every method can be simplified with just Get()
time.sleep(1)
t.Get(search_string = "Torrent Name", search_IMDB = "tt123456", search_TVDB = "123456", search_moviedb = "123456", 
category = Category.ALL, limit = 25, sort = Sort.LAST, min_seeders = 10, min_leechers = 10, extended = False, 
ranked = True)