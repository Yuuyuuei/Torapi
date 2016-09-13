# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests, time
from Filters import Category, Sort

BASE_URL = "https://torrentapi.org/pubapi_v2.php"
TOKEN_URL = BASE_URL + "?get_token=get_token"

# Torapi().Search(filter).json();
class Torapi(object):
	def __init__(self, *args):
		super(Torapi, self).__init__(*args)
		self.Filter = ""
		self._searched = False

	def List(self):
		self.Filter = self.Filter + "&mode=list"
		return self

	def SearchTheMovieDB(self, id):
		self.Filter = self.Filter + "&mode=search&search_themoviedb={0}".format(id)
		self._searched = True
		return self

	def SearchIMDB(self, id):
		self.Filter = self.Filter + "&mode=search&search_imdb={0}".format(id)
		self._searched = True
		return self

	def SearchTVDB(self, id):
		self.Filter = self.Filter + "&mode=search&search_tvdb={0}".format(id)
		self._searched = True
		return self

	def Search(self, string):
		self.Filter = self.Filter + "&mode=search&search_string={0}".format(string)
		self._searched = True
		return self

	def Category(self, category = Category.ALL):
		self.Filter = self.Filter + "&category=" + category
		return self

	def Limit(self, integer = 25):
		self.Filter = self.Filter + "&limit=" + str(integer)
		return self

	def Sort(self, sort = Sort.LAST):
		self.Filter = self.Filter + "&sort=" + sort
		return self

	def MinSeeders(self, integer = 0):
		self.Filter = self.Filter + "&min_seeders={0}".format(integer)
		return self

	def MinLeechers(self, integer = 0):
		self.Filter = self.Filter + "&min_leechers={0}".format(integer)
		return self

	def Extended(self, boolean = False):
		if boolean:
			self.Filter = self.Filter + "&format=json_extended"
		else:
			self.Filter = self.Filter + "&format=json"
		return self

	def Ranked(self, boolean = True):
		if boolean:
			self.Filter = self.Filter + "&ranked=1"
		else:
			self.Filter = self.Filter + "&ranked=0"
		return self

	def Get(self, search_string = None, search_IMDB = None, search_TVDB = None, search_moviedb = None, 
	category = None, limit = None, sort = None, min_seeders = None, min_leechers = None, extended = False, 
	ranked = True):
		token = Torapi.GetToken()

		if not search_string and not search_IMDB and not search_TVDB and not search_moviedb and not self._searched:
			self.List()
		
		if search_string:
			self.Search(search_string)

		if search_IMDB:
			self.SearchIMDB(search_IMDB)

		if search_TVDB:
			self.SearchTVDB(search_TVDB)

		if search_moviedb:
			self.SearchTheMovieDB(search_moviedb)

		if category:
			self.Category(category)

		if limit:
			self.Limit(limit)

		if sort:
			self.Sort(sort)

		if min_seeders:
			self.MinSeeders(min_seeders)

		if min_leechers:
			self.MinLeechers(min_leechers)

		if extended:
			self.Extended(extended)

		if not ranked:
			self.Ranked(ranked)

		r = requests.get(BASE_URL + "?token=" + token + self.Filter)
		return r.json()

	@staticmethod
	def GetToken():
		""" Gets a token required to make other requests """
		request = requests.get(TOKEN_URL)
		token = request.json()["token"]
		return token