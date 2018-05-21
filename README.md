genius-trending.py
==================

**genius-trending.py** is a Python API for downloading the top 10 trending songs from [Genius.com](https://www.genius.com).

Installation
------------
You can install **genius-trending.py** with pip by executing the following:
```
pip install genius-trending.py 
```

Quickstart
----------
To download the trending songs on Genius, we need to construct a `GeniusData` object.

```Python
>>> import genius_trending as genius
>>> trending = genius.GeniusData()
```
Now, let's take a look at what information is available in each `SongEntry`!
```Python
>>> song = trending[0]
>>> print(song.title)
This is America
>>> print(song.artist)
Childish Gambino
>>> print(song.rank)
1
```

We even have the option of printing the entire trending songs chart!

```Python
>>> print(trending)
Top 10 songs on Genius as of 10:00PM on May 20, 2018
----------------------------------------------------
1. This is America by Childish Gambino
2. Fake Love by BTS
3. Yes Indeed by Lil Baby & Drake
#...
```
Contributing
------------
Feel free to submit a pull requests! 
If you found a bug or would like to request something else, create an issue [here](https://www.github.com/kennyrozario/genius-trending/issues).

Dependencies
------------
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://requests.readthedocs.org/en/latest/) 

License
-------
* This project is licensed under the MIT License.
* The Genius trending information is owned by Genius Media Group Inc. See Genius.com's [Terms of Use](https://genius.com/static/terms) for more information.
