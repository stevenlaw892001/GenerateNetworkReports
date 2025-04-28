# Network Traffic PDF Generator

This Python script uses Playwright to generate PDF reports from network traffic monitoring URLs. It saves the PDFs with dynamic file names based on the current date.

## Prerequisites

- Python 3.8+
- Playwright for Python
- python-dotenv for environment variable management

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install  # Install browser binaries
   ```

3. **Configure environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and fill in your actual values for `OUTPUT_DIR` and the URLs.

4. **Run the script**:
   ```bash
   python generate_network_reports.py
   ```

## Configuration

- **`OUTPUT_DIR`**: Directory where PDFs will be saved (default: `output/`).
- **`URL_*`**: URLs for the network traffic pages to convert to PDFs.
- Set `headless=True` in the script for production to run without a visible browser.

## Output

The script generates PDFs in the specified `OUTPUT_DIR` with names like:
- `Network Traffic Combined YYYY-MM-DD.pdf`
- `Network Traffic Network1 YYYY-MM-DD.pdf`
- `Network Traffic Network2 YYYY-MM-DD.pdf`

## Notes

- Ensure the URLs are accessible and the output directory has write permissions.
- Logs are generated to track progress and errors.
- For internal URLs, use a VPN or ensure the script runs in the appropriate network environment.

## Contributing

We welcome contributions to this project! Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before participating to ensure a respectful and inclusive environment. To contribute, please submit a pull request or open an issue on the GitHub repository.

## License

MIT License