from playwright.sync_api import Page, expect, sync_playwright
import os

def test_pdf_single_page_ui(page: Page):
    file_path = "file://" + os.path.abspath("index.htm")
    page.goto(file_path)

    # 1. Open settings drawer
    page.click("#open-settings")

    # 2. Check for updated UI text
    expect(page.get_by_text("Gera um arquivo PDF com um mês por página")).to_be_visible()

    # 3. Take a screenshot
    page.screenshot(path="verification/updated_drawer_ui.png")

    # 4. Trigger PDF generation
    page.click("#download-pdf")
    expect(page.locator("#download-pdf")).to_contain_text("GERANDO PDF")

    page.screenshot(path="verification/generating_pdf_single.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_pdf_single_page_ui(page)
        finally:
            browser.close()
