# DjangoCon(DJNGC): Holistiplan Assessment

## Disclaimer

>Make sure you have initialized the application by following the execution steps at: `https://github.com/ocrfin/qa_homework/`.<br>
>The holistiplan app must be running at `http://localhost:3000`

## Directory Guide

```
qa_eng_task/
├── pages/                  # Page Object Model classes
├── tests/                  # Test suites
├── documentation/          # Testing documentation
    ├──── manual_testing.md # Manual testing report
    ├ automation_testing.md # Automation testing report
├── conftest.py             # Pytest configuration
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
└── .gitignore              # Git ignore rules
```

## Setup Guide

### 1. Create a fork from this repository

```bash
git clone <fork-github.com/lpereiras/qa_eng_task>
cd qa_eng_task
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt indicating the virtual environment is active.

### 3. Install Python Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

### 5. Verify Application status (double check)

Before running tests, ensure the application is running:

1. Open your browser and navigate to `http://localhost:3000`
2. You should see the DjangoCon rewards page
3. If not, follow the instructions again at [qa_homework repository](https://github.com/ocrfin/qa_homework/)

### 6. Run the Tests

**Run all tests:**
```bash
pytest
```

**Run all tests generating pytest report:**
```bash
pytest --html=report
```

**Run specific test file:**
```bash
pytest tests/e2e/test_auth.py
pytest tests/e2e/test_rewards.py
```

**Run a single test:**
```bash
pytest -k test_signup_with_valid_credentials
```

**Run test in debug mode:**
```bash
PWDEBUG=1 pytest -k test_signup_with_valid_credentials
```
