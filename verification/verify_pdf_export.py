from playwright.sync_api import Page, expect, sync_playwright
import os

def test_pdf_export_ui(page: Page):
    # Get absolute path to index.htm
    file_path = "file://" + os.path.abspath("index.htm")
    page.goto(file_path)

    # 1. Open settings drawer
    page.click("#open-settings")

    # 2. Check if PDF Export section exists
    expect(page.get_by_text("Exportar PDF (A4)")).to_be_visible()

    # 3. Check if inputs exist and are initialized
    expect(page.locator("#pdf-start-month")).to_be_visible()
    expect(page.locator("#pdf-start-year")).to_be_visible()
    expect(page.locator("#pdf-end-month")).to_be_visible()
    expect(page.locator("#pdf-end-year")).to_be_visible()

    # 4. Take a screenshot of the drawer
    page.screenshot(path="verification/drawer_ui.png")

    # 5. Click Download PDF and check button text
    # We expect it to change to "GERANDO PDF..."
    page.click("#download-pdf")
    expect(page.locator("#download-pdf")).to_contain_text("GERANDO PDF")

    # Take another screenshot during generation
    page.screenshot(path="verification/generating_pdf.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_pdf_export_ui(page)
        finally:
            browser.close()
