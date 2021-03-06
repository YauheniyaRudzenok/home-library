# Based on Goodreads.py, by Owen Mellema
# https://github.com/architectdrone/goodreads.py/blob/master/goodreads.py

import requests
from xml.etree import ElementTree


with open("goodreads_auth.txt") as f:
    key = f.read()


class GoodreadsRequest:
    '''
    Represents a single request to Goodreads.
    '''

    def __init__(self, endpoint, special_endpoint=False, parameters=None):
        global key
        if endpoint is None:
            AssertionError("Unfortunately, there is no endpoint for looking up this data.")

        if special_endpoint:
            url = endpoint
        else:
            url = "https://www.goodreads.com/{endpoint}".format(endpoint=endpoint)

        if "key=" not in url: 
            url = url + "?key={key}".format(key=key)

        if parameters is not None:
            for param in parameters:
                url = url + "&{param}={value}".format(param=param, value=parameters[param])

        resp = requests.get(url)
        self.response = ElementTree.fromstring(resp.content)
        self.response = self.response[1] #The first entry is always just unneeded stuff.

        self.success = resp.status_code == 200

class GoodreadsData:
    '''
    Parent class for all objects that store goodreads data.

    This class does things like cacheing results.
    '''
    def __init__(self, incomplete_tree=None):
        '''
        incomplete_tree is an Element Tree containing partial information about the data. Some parents have a partial tree containing some information. This can be cached to save a request.
        '''
        self.response = None #When a request is made, it is stored in memory. This assumes that a piece of data will never update within the lifetime of the program.
        self.cache = {}
        self.special_endpoint = False #When an endpoint requires more sturcture than what is currently present
        self.parameters = {}

        # Handle Cacheing
        if incomplete_tree is not None:
            for i in incomplete_tree:
                self.cache[i.tag] = i

    def id(self):
        return self.id

    def _request(self, lookup_value, returnText = True):
        '''
        Returns the desired data.
        lookup_value: A string that holds the data that is wanted.
        returnText: Whether to return an elementTree or a string
        '''
        if lookup_value in self.cache: #First we check if the data is in the incomplete tree cache.
            result = self.cache[lookup_value]
        else: #If not, we look at an actual request
            self.make_request()
            result = self.response.find(lookup_value)

        if returnText:
            return result.text
        else:
            return result


    def make_request(self):
        if self.response is None: #We check if there is a request already present before making a request
            self.response = GoodreadsRequest(self.endpoint, special_endpoint=self.special_endpoint, parameters=self.parameters).response


    def parseDataList(self, tree, the_class, search_pattern: str="id"):
        '''
        Parses an element tree that is comprised of elements that are objects previously created.
        tree: The elementTree to parse.
        the_class: The class to store the data in.
        '''
        return [the_class(i.find(search_pattern), incomplete_tree=i) for i in tree]

class Author(GoodreadsData):
    def __init__(self, id, incomplete_tree=None):
        GoodreadsData.__init__(self, incomplete_tree=incomplete_tree)
        self.id = id
        self.endpoint = "author/show/{id}".format(id=self.id)

    def __repr__(self):
        return self.name()

    def name(self):
        return self._request("name")

    # def fans(self):
    #     return self._request("fans_count")

    # def about(self):
    #     return self._request("about")
    
    # def influences(self):
    #     return self._request("influences")
    
    # def works_count(self):
    #     return self._request("works_count")
    
    # def gender(self):
    #     return self._request("gender")
    
    # def hometown(self):
    #     return self._request("hometown")
    
    # def born(self):
    #     return self._request("born_at")
    
    # def died(self):
    #     return self._request("died_at")
    
    # def books(self):
    #     all_books = self._request("books", returnText=False)
    #     return self.parseDataList(all_books, Book)

class Book(GoodreadsData):
    def __init__(self, id, incomplete_tree=None):
        GoodreadsData.__init__(self, incomplete_tree=incomplete_tree)
        self.id = id if type(id) is int else id.text
        self.endpoint = "book/show/{id}".format(id=self.id)  

    def __repr__(self):
        return self.title()

    def title(self):
        return self._request("title")
    
    # def isbn(self):
    #     return self._request("isbn")
    
    # def country(self):
    #     return self._request("country_code")

    # def year(self):
    #     return self._request("publication_year")

    # def month(self):
    #     return self._request("publication_month")
    
    # def day(self):
    #     return self._request("publication_day")
    
    # def publisher(self):
    #     return self._request("publisher")
    
    # def language(self):
    #     return self._request("language_code")
    
    def description(self):
        return self._request("description")
    
    # def average_rating(self):
    #     return self._request("average_rating")
    
    # def page_count(self):
    #     return self._request("num_pages")

    # def format(self):
    #     return self._request("format")
    
    # def edition_information(self):
    #     return self._request("edition_information")
    
    # def ratings_count(self):
    #     return self._request("ratings_count")
    
    # def review_count(self):
    #     return self._request("text_reviews_count")

    # def goodreads_url(self):
    #     return self._request("url")

    def image_url(self):
        return self._request("image_url")
    
    def authors(self):
        authors = self._request("authors", returnText=False)
        return self.parseDataList(authors, Author)
    
    # def popular_shelves(self):
    #     shelves = self._request("popular_shelves", returnText=False)
    #     return self.parseDataList(shelves, Shelf)

    # def similar_books(self):
    #     books = self._request("similar_books", returnText=False)
    #     return self.parseDataList(books, Book)

class Shelf(GoodreadsData):
    def __init__(self, id, incomplete_tree=None):
        GoodreadsData.__init__(self, incomplete_tree=incomplete_tree)
        self.id = id
        self.endpoint = None
    
    def __repr__(self):
        return self.name()

    def name(self):
        return self._request("name")
    
    def book_count(self):
        return self._request("book_count")
    
    def exclusive(self):
        return self._request("exclusive_flag")
    
    def description(self):
        return self._request("description")

class User(GoodreadsData):
    def __init__(self, id, incomplete_tree=None):
        GoodreadsData.__init__(self, incomplete_tree=incomplete_tree)
        self.id = id
        self.endpoint = "user/show/{id}".format(id=id)
    
    def name(self):
        return self._request("name")
    
    def user_name(self):
        return self._request("user_name")
    
    def about(self):
        return self._request("about")
    
    def age(self):
        return self._request("age")
    
    def gender(self):
        return self._request("gender")
    
    def location(self):
        return self._request("location")
    
    def website(self):
        return self._request("website")
    
    def joined(self):
        return self._request("joined")
    
    def last_active(self):
        return self._request("last_active")
    
    def interests(self):
        return self._request("interests")
    
    def favorite_authors(self):
        authors = self._request("favorite_authors", returnText=False)
        return self.parseDataList(authors, Author)
    
    def favorite_books(self):
        books = self._request("favorite_books", returnText=False)
        return self.parseDataList(books, Book)
    
    def friends_count(self):
        return self._request("friends_count")
    
    def user_shelves(self):
        shelves = self._request("user_shelves", returnText=False)
        return self.parseDataList(shelves, Shelf)
    

class SearchBooks(GoodreadsData):
    def __init__(self, query: str, incomplete_tree=None):
        GoodreadsData.__init__(self, incomplete_tree=incomplete_tree)
        self.endpoint = "search/index.xml"
        self.special_endpoint = False
        self.parameters['q'] = query


    def books(self):
        self.make_request()
        return self.parseDataList(self.response.findall("./results/work/best_book"), Book)