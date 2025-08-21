from playwright.sync_api import expect
import re
from random import randint
from page_objects.landing_page import HackerNews

# 1. Verify stories have title

def test_story_title(page):
    hacker_news = HackerNews(page)
    hacker_news.navigate()

    title_rows = hacker_news.get_title_rows()
    expect(title_rows).not_to_have_count(0)

    count = title_rows.count()
    for i in range(count):
        title_rank = hacker_news.get_title_rank(row=title_rows, index=i)
        title = hacker_news.get_title_text(row=title_rows, index=i)
        assert title, f"title missing for {title_rank}"

# 2. Verify each story has a valid url

def test_story_link(page):
    hacker_news = HackerNews(page)
    hacker_news.navigate()

    title_rows = hacker_news.get_title_rows()
    expect(title_rows).not_to_have_count(0)

    count = title_rows.count()
    for i in range(count):
        title_rank = hacker_news.get_title_rank(row=title_rows, index=i)
        title_link = hacker_news.get_title_link(row=title_rows, index=i)
        assert title_link, f"Story missing for: {title_rank}"
        if not title_link.startswith("http"):
            print(f"{title_rank} {title_link} is an HN internal link")

# 3. Verify 'new' menu option url

def test_new_stories(page):
    hacker_news = HackerNews(page)
    hacker_news.navigate()
    hacker_news.click_new()
    expect(page).to_have_url(re.compile(".*newest"))

# 4. Verify on clicking a random story the correct  external link opens and title is valid

def test_open_link(page):
    hacker_news = HackerNews(page)
    hacker_news.navigate()
    title_rows = hacker_news.get_title_rows()
    count = title_rows.count()
    assert count > 0, "No title available"
    random_index = randint(0,count-1)
    title_link = hacker_news.get_title_link(row=title_rows, index=random_index)
    title = hacker_news.get_title_text(row=title_rows, index=random_index)
    print(title)
    assert title_link, "Link not available"
    hacker_news.click_link(row=title_rows, index=random_index)
    expect(page).to_have_url(title_link, timeout=10000)



# 5. Verify the subtext for a random story

def test_subtext(page):
    hacker_news = HackerNews(page)
    hacker_news.navigate()
    title_rows = hacker_news.get_title_rows()
    count = title_rows.count()
    assert count > 0, "No titles available"
    random_index = randint(0, count-1)
    subtitle = hacker_news.get_subtitle_row(row=title_rows, index=random_index)
    score = hacker_news.get_score(subtitle_row=subtitle)
    author = hacker_news.get_author(subtitle_row=subtitle)
    comment = hacker_news.get_comment(subtitle_row=subtitle)
    expect(score).to_have_text(re.compile(r"\d+ points?"))
    expect(author).to_have_text(re.compile(r".+"), use_inner_text=True)
    expect(comment).to_have_text(re.compile(r"\d+\s*comments?"))




    



