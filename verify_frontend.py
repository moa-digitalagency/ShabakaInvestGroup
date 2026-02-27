from playwright.sync_api import sync_playwright

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Go to home page
        page.goto("http://localhost:5000")

        # Take a screenshot of the header
        page.screenshot(path="verification_header.png", clip={"x": 0, "y": 0, "width": 1920, "height": 100})

        # Scroll to footer and take a screenshot
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="verification_footer.png", clip={"x": 0, "y": 500, "width": 1920, "height": 800}) # approximate footer area

        browser.close()

if __name__ == "__main__":
    verify_changes()