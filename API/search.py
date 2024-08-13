from icrawler.builtin import GoogleImageCrawler

class image():
    def __init__(self, titel):
        self.titel = titel

    def get_image(self):
        google_crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
        google_crawler.crawl(keyword=self.titel , max_num=10)
