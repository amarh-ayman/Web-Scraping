from web_scraper import __version__ 
from web_scraper.scraper import *


def test_version():
    assert __version__ == '0.1.0'

def test_count():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico") == 5 


def test_report():
    actual = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")[0][0][:62]
    expected = 'The written history of Mexico spans more than three millennia.'
    assert actual == expected