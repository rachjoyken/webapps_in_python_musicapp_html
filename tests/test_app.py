from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    page.screenshot(path="screenshot.png", full_page=True)
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        'Hypnotised'
    ])
    expect(paragraph_tags).to_have_text([
        '1980'
    ])