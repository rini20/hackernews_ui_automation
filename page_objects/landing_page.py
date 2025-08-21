# Hacker News landing page POM
import re

class HackerNews:

    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto("https://news.ycombinator.com/")

    def get_title_rows(self):
        return self.page.locator("tr.athing")


    def get_title_rank(self,row, index):
         return row.nth(index).locator("span.rank").inner_text()


    def get_title_link(self, row, index):
        title_a = row.nth(index).locator("span.titleline > a").first
        return title_a.get_attribute("href")

    def get_title_text(self, row, index):
        title_a = row.nth(index).locator("span.titleline > a").first
        return title_a.inner_text().strip()

    def click_link(self, row, index):
        return row.nth(index).locator("span.titleline > a").first.click()

    def click_new(self):
        self.page.get_by_role("link", name="new", exact=True).click()


    def get_subtitle_row(self, row, index):
        return row.nth(index).locator("+ tr")

    def get_score(self, subtitle_row):
        return subtitle_row.locator(".score")

    def get_author(self, subtitle_row):
        return subtitle_row.locator("a.hnuser")

    def get_comment(self, subtitle_row):
        return subtitle_row.locator("a").filter(has_text=re.compile(r"comment"))



