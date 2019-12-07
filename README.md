Torapi
============

Unofficial http://torrentapi.org/ API library

https://torrentapi.org/apidocs_v2.txt

**The api has a 1req/2s limit.**

Installation
------------

```
pip install requests
python setup.py install

Run this to test if it was successful
python torapi_test.py

Successful if no error returns
```

Usage
------------

```python
from Torapi import Torapi
from Torapi.Filters import *
import time

t = Torapi()

# Everything is returned in JSON
# !! IMPORTANT: Notice the time.sleep(1) before each Get() request
# !! The api has a 1req/2s limit.

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
```

Categories
------------

Category.*

* ALL
* XXX
* NON_XXX
* MUSIC
* MUSIC_MP3
* MUSIC_FLAC
* EBOOKS
* MOVIES
* MOVIES_FULL_BD
* MOVIES_X264_1080
* MOVIES_X264_720
* MOVIES_BD_REMUX
* MOVIES_X264_3D
* MOVIES_XVID_720
* MOVIES_XVID
* MOVIES_X264
* TV
* TV_SHOWS
* TV_EPISODES
* TV_HD_EPISODES
* GAMES
* GAMES_PS3
* GAMES_PC_ISO
* GAMES_PC_RIP
* GAMES_XBOX360
* SOFTWARE
* SOFTWARE_PC_ISO
```
