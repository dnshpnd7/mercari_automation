# Mercari Playwright Test Automation Framework

## Folder Structure

The following structure represents the organization of the framework:

```
project-directory/
├── pages/
│   ├── home_page.py
│   ├── category_page.py
│   └── base_page.py
├── reports/
│   ├── test_report.html
├── tests/
│   ├── test_mercari.py
├── conftest.py
├── pytest.ini
├── README.md
```

### Description of Folders and Files

1. **pages/**: Contains Page Object Model (POM) classes for defining web elements and actions for specific pages.
   - `home_page.py`: Page object for the home page.
   - `category_page.py`: Page object for category selection.
   - `base_page.py`: Base class with reusable methods for interacting with web elements.

2. **reports/**: Stores test execution reports.
   - `test_report.html`: Generated HTML report for the test run.

3. **tests/**: Contains test scripts.
   - `test_mercari_search_conditions.py`: Test case for validating Mercari search functionality.

4. **conftest.py**: Contains shared fixtures for the test suite.

5. **pytest.ini**: Configuration file for pytest options.

6. **README.md**: Documentation for the framework.

## Installation and Setup

### Prerequisites
- Python 3.7+
- Node.js (for Playwright installation)

### Installation Steps

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd project-directory
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Install Playwright:
   ```sh
   playwright install
   ```

## Running Tests

1. Execute tests:
   ```sh
   pytest
   ```

2. Generate an HTML report:
   ```sh
   pytest --html=reports/test_report.html --self-contained-html
   ```

## Configuration

### pytest.ini

This file contains pytest configurations:
```ini
[pytest]
addopts = --html=reports/test_report.html --self-contained-html
log_cli = true
```

### conftest.py

Defines shared fixtures for browser and test setup:
```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
```

## Framework Usage

1. **Page Object Model**:
   - Add methods and locators for new pages in the `pages/` folder.

2. **Writing Tests**:
   - Write test cases in the `tests/` folder, importing page objects as needed.

3. **Generating Reports**:
   - Run pytest with the `--html` option to generate an HTML report.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature-name'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

