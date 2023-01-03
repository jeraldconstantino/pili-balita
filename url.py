# the URL link should be modified based on the URL generated in your Heroku account.
# Take note of "news" parameter in the URL link.
def get_url(news):
    URL = f"https://pilibalita-api.herokuapp.com/hula?balita={news}"
    return URL