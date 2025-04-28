# Contributing to Network Traffic PDF Generator

We welcome contributions to the Network Traffic PDF Generator project! Whether you're fixing bugs, adding features, improving documentation, or suggesting ideas, your help is appreciated. This document outlines how to contribute effectively.

## Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. We expect all contributors to adhere to these guidelines to ensure a respectful and inclusive environment.

## How to Contribute

### Reporting Issues

If you encounter bugs, have feature requests, or want to suggest improvements:
1. Check the [GitHub Issues](https://github.com/your-username/your-repo/issues) to see if the issue has already been reported.
2. If not, open a new issue and provide:
   - A clear title and description.
   - Steps to reproduce the issue (if applicable).
   - Expected and actual behavior.
   - Any relevant screenshots or logs.

### Submitting Pull Requests

To contribute code or documentation changes:
1. **Fork the repository** and create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** in your branch. Ensure your code follows the project's style and structure.
3. **Test your changes** locally:
   - Install dependencies: `pip install -r requirements.txt` and `playwright install`.
   - Run the script: `python generate_network_reports.py`.
   - Verify that your changes work as expected.
4. **Commit your changes** with a clear message:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```
5. **Push to your fork** and submit a pull request (PR) to the `main` branch of the original repository:
   ```bash
   git push origin feature/your-feature-name
   ```
6. In the PR description, include:
   - What the PR does.
   - Why it is needed.
   - Any related issues (e.g., "Fixes #123").

### Development Setup

To set up the project for development:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Copy `.env.example` to `.env` and configure it with test URLs and an output directory:
   ```bash
   cp .env.example .env
   ```
4. Run the script to test your changes:
   ```bash
   python generate_network_reports.py
   ```

### Contribution Guidelines

- **Code Style**: Follow Python PEP 8 guidelines. Use clear, descriptive variable names and include comments where necessary.
- **Testing**: Ensure your changes do not break existing functionality. Test with different URLs and output directories if possible.
- **Documentation**: Update `README.md` or other documentation if your changes affect setup, configuration, or usage.
- **Scope**: Keep pull requests focused on a single feature or fix to make review easier.

## Getting Help

If you have questions or need assistance, feel free to:
- Open an issue on the [GitHub repository](https://github.com/your-username/your-repo/issues).
- Contact the maintainers via [insert contact method, e.g., email or GitHub Issues].

Thank you for contributing to the Network Traffic PDF Generator!