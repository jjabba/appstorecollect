from argparse import ArgumentError

class Collector():
    country_codes = ['us', 'ca', 'se']
    app_id = None
    country_code = None

    def __init__(self, app_id, country_code='us'):
        if country_code not in self.country_codes:
            raise ValueError("The country code provided is unkown or invalid! (%s)" % country_code)

        self.country_code = country_code
        self.app_id = app_id

    def feed_url(self):
        return "https://itunes.apple.com/%s/rss/customerreviews/id=%s/sortBy=mostRecent/json" % (self.country_code, self.app_id)
