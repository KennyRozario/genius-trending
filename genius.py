#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import datetime


class SongEntry:
    """ Represents a single trending song on the genius.com home page.

    Attributes:
        title: The title of the song.
        artist: The name of the song artist, as formatted on Genius.com.
            If there are multiple artists and/or features, they will be
            included within this string.
        rank: The song's position on the chart, as an int.
    """

    def __init__(self, title, artist, rank):
        self.title = title
        self.artist = artist
        self.rank = rank

    def __repr__(self):
        """Returns a string in the form: 'TITLE by Artist
        """
        return '{} by {}'.format(self.title, self.artist)


class GeniusData:
    """ Represents the top 10 songs at the time of instantiation on Genius.com

    Attributes:
        entries: A list of SongEntry objects, ordered by position on the chart
        (highest first).
    """

    def __init__(self):
        self.entries = []
        self.fetch_entries()

    def __repr__(self):
        """Returns the chart as a human-readable string
        """
        s = 'Top 10 songs on Genius as of {}'.format(datetime.datetime.now().strftime('%l:%M%p on %b %d, %Y'))
        s += '\n' + '-' * len(s)

        for entry in self.entries:
            s += '\n{}. {} by {}'.format(entry.rank, entry.title, entry.artist)

        return s

    def __len__(self):
        """Returns the number of entries in the chart.
        A length of zero may indicated a failed/bad request.
        """
        return len(self.entries)

    def fetch_entries(self):
        """GETs the trending songs from Genius.com,
        then parses the data using BeautifulSoup
        """

        url = 'https://www.genius.com'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        for row in soup.find_all(class_="chart_row"):
            rank = row.find(class_="chart_row-number_container-number").text.strip()

            title_and_artist_html = row.find(class_="chart_row-two_line_title_and_artist")
            if title_and_artist_html:
                title_and_artist = title_and_artist_html.text.strip().split('\n      ')
                title, artist = title_and_artist[0], title_and_artist[1]
            else:
                title_and_artist = row.find(class_="chart_row-content").text.split(' by ')
                title, artist = title_and_artist[0], title_and_artist[1]

            entry = SongEntry(title, artist, rank)
            self.entries.append(entry)
