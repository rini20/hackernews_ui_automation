# Hacker News landing page POM

class HackerNews:

    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto("https://news.ycombinator.com/")

    def get_title_rows(self):
        return self.page.locator("tr.athing")


    def get_title_rank(self,row, index):
         return row.nth(index).locator("span.rank").inner_text()

    def get_title(self, row, index):
        return row.nth(index).locator("span.titleline > a").inner_text().strip()
