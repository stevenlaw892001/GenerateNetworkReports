import re
import time
import datetime
import os
import logging
from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging for tracking script execution and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Get today's date for dynamic file naming
today_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Get output directory from environment variable or use default
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure output directory exists

# Define tasks with URLs and corresponding file names
# Note: Replace placeholder URLs with actual ones in a .env file
tasks = [
    {
        "url": os.getenv("URL_NETWORK_COMBINED", "https://example.com/networktraffic/combined"),
        "file_name": f"Network Traffic Combined {today_date}.pdf",
    },
    {
        "url": os.getenv("URL_NETWORK1", "https://example.com/networktraffic/network1"),
        "file_name": f"Network Traffic Network1 {today_date}.pdf",
    },
    {
        "url": os.getenv("URL_NETWORK2", "https://example.com/networktraffic/network2"),
        "file_name": f"Network Traffic Network2 {today_date}.pdf",
    },
]

def run(playwright: Playwright) -> None:
    """Generate PDF reports from network traffic URLs using Playwright."""
    browser = None
    context = None
    try:
        # Launch Chromium browser (headless=False for debugging, set to True for production)
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Process each task to generate a PDF
        for task in tasks:
            logger.info(f"Processing URL: {task['url']}")
            try:
                # Navigate to the URL and wait for full page load
                page.goto(task["url"])
                page.wait_for_load_state("networkidle")  # Ensure network activity is complete

                # Emulate print media for PDF generation
                page.emulate_media(media="print")

                # Save the page as a PDF to the output directory
                output_path = os.path.join(OUTPUT_DIR, task["file_name"])
                page.pdf(path=output_path)
                logger.info(f"Saved PDF: {output_path}")

            except Exception as e:
                logger.error(f"Failed to process {task['url']}: {str(e)}")

    except Exception as e:
        logger.error(f"An error occurred during execution: {str(e)}")

    finally:
        # Clean up resources
        if context:
            context.close()
            logger.info("Browser context closed")
        if browser:
            browser.close()
            logger.info("Browser closed")

def main():
    """Entry point for the script."""
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    main()