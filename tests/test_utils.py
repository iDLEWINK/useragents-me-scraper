from useragents_me_scraper import utils


def test_is_outdated():
    assert utils.is_outdated('2000-01-01') == True


def test_is_not_outdated():
    assert utils.is_outdated('2099-01-01') == False
