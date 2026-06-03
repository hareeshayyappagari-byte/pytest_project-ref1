# 🚀 PyTest Complete Cheat Sheet for QA Automation Engineers

## 📌 1. Basic Test Execution

| Command | Description |
|----------|------------|
| `pytest` | Run all test cases |
| `pytest test_login.py` | Run specific file |
| `pytest tests/` | Run all tests inside folder |
| `pytest tests/smoke/` | Run tests from specific directory |

---

## 📌 2. Run Specific Test

### Run Single Test Method

```bash
pytest test_login.py::test_valid_login
```

Example:

```python
def test_valid_login():
    pass
```

---

### Run Specific Class

```bash
pytest test_login.py::TestLogin
```

Example:

```python
class TestLogin:

    def test_valid_login(self):
        pass

    def test_invalid_login(self):
        pass
```

---

## 📌 3. Output & Logging

| Command | Description |
|----------|------------|
| `pytest -v` | Verbose output |
| `pytest -vv` | Extra verbose output |
| `pytest -s` | Display print statements |
| `pytest -ra` | Extra summary info |
| `pytest -l` | Show local variables on failure |

Example:

```python
def test_demo():
    print("Automation Testing")
```

```bash
pytest -s
```

---

## 📌 4. Test Selection

### Run by Keyword

```bash
pytest -k login
```

```bash
pytest -k "login and valid"
```

```bash
pytest -k "login or signup"
```

```bash
pytest -k "not login"
```

---

### Run by Marker

```bash
pytest -m smoke
```

```python
@pytest.mark.smoke
def test_login():
    pass
```

Multiple Markers:

```bash
pytest -m "smoke or regression"
pytest -m "smoke and regression"
pytest -m "not smoke"
```

---

## 📌 5. Failure Handling

| Command | Purpose |
|----------|----------|
| `pytest -x` | Stop after first failure |
| `pytest --maxfail=2` | Stop after 2 failures |
| `pytest --lf` | Run last failed tests |
| `pytest --ff` | Failed tests first |
| `pytest --pdb` | Open debugger on failure |

---

## 📌 6. Debugging

### Manual Debugging

```python
import pdb

def test_demo():
    pdb.set_trace()
```

Run:

```bash
pytest -s
```

---

## 📌 7. Fixtures

### Show Available Fixtures

```bash
pytest --fixtures
```

### Detailed Fixture Info

```bash
pytest --fixtures -v
```

---

## 📌 8. Test Collection

### Collect Tests Only

```bash
pytest --collect-only
```

Useful for checking discovered tests.

---

## 📌 9. Parallel Execution

### Install

```bash
pip install pytest-xdist
```

### Execute

```bash
pytest -n 4
```

Use All CPU Cores:

```bash
pytest -n auto
```

---

## 📌 10. HTML Reporting

### Install

```bash
pip install pytest-html
```

### Generate Report

```bash
pytest --html=report.html
```

### Self Contained Report

```bash
pytest --html=report.html --self-contained-html
```

---

## 📌 11. Allure Reporting

### Install

```bash
pip install allure-pytest
```

### Generate Results

```bash
pytest --alluredir=allure-results
```

### Generate Report

```bash
allure serve allure-results
```

---

## 📌 12. Coverage Reporting

### Install

```bash
pip install pytest-cov
```

### Run Coverage

```bash
pytest --cov=project
```

### HTML Coverage

```bash
pytest --cov=project --cov-report=html
```

### Terminal Coverage

```bash
pytest --cov=project --cov-report=term-missing
```

---

## 📌 13. Repeat Test Execution

### Install

```bash
pip install pytest-repeat
```

### Run 5 Times

```bash
pytest --count=5
```

Useful for flaky test analysis.

---

## 📌 14. Traceback Options

### Long Traceback

```bash
pytest --tb=long
```

### Short Traceback

```bash
pytest --tb=short
```

### No Traceback

```bash
pytest --tb=no
```

---

## 📌 15. Warning Management

Disable warnings:

```bash
pytest --disable-warnings
```

---

## 📌 16. JUnit XML Report (Jenkins)

```bash
pytest --junitxml=result.xml
```

Used by Jenkins for publishing test results.

---

## 📌 17. Environment Variables

Linux/Mac:

```bash
ENV=QA pytest
```

Windows:

```cmd
set ENV=QA && pytest
```

Example:

```python
import os

env = os.getenv("ENV")
print(env)
```

---

## 📌 18. Useful pytest.ini

```ini
[pytest]
addopts = -v -s

markers =
    smoke
    regression
    sanity
    ui
    api
```

Run:

```bash
pytest
```

Automatically applies configured options.

---

# 🔥 Advanced Commands Used in Real-Time Projects

## Run Smoke Suite

```bash
pytest -m smoke -v
```

## Run Regression Suite

```bash
pytest -m regression -v
```

## Execute API Tests

```bash
pytest -m api -v
```

## Execute UI Tests

```bash
pytest -m ui -v
```

## Execute Specific Browser

```bash
pytest --browser chrome
pytest --browser firefox
pytest --browser edge
```

Example:

```python
def pytest_addoption(parser):
    parser.addoption("--browser")
```

---

## Generate Logs

```bash
pytest --log-cli-level=INFO
```

```bash
pytest --log-file=logs/test.log
```

---

## Capture Screenshots on Failure

```python
@pytest.hookimpl
def pytest_exception_interact(node, call, report):
    driver.save_screenshot("failure.png")
```

---

## Retry Failed Tests

Install:

```bash
pip install pytest-rerunfailures
```

Run:

```bash
pytest --reruns 2
```

```bash
pytest --reruns 2 --reruns-delay 5
```

---

## Execution Duration Report

```bash
pytest --durations=10
```

Shows top 10 slowest tests.

---

## Run Tests Randomly

Install:

```bash
pip install pytest-randomly
```

```bash
pytest
```

Useful for finding dependency issues.

---

# 🚀 Jenkins Pipeline Command

```bash
pytest tests/ \
-v \
-s \
-m smoke \
--html=reports/report.html \
--self-contained-html \
--junitxml=reports/result.xml
```

---

# 🚀 CI/CD Enterprise Command

```bash
pytest tests/ \
-v \
-s \
-n auto \
--reruns 2 \
--cov=. \
--cov-report=html \
--html=reports/report.html \
--self-contained-html \
--junitxml=reports/result.xml
```

---

# ⭐ Top 20 Commands Every QA Automation Engineer Uses

```bash
pytest -v
pytest -s
pytest -x
pytest --lf
pytest --ff
pytest -k login
pytest -m smoke
pytest -m regression
pytest -n auto
pytest --html=report.html
pytest --junitxml=result.xml
pytest --cov=.
pytest --cov-report=html
pytest --pdb
pytest --fixtures
pytest --collect-only
pytest --tb=short
pytest --reruns 2
pytest --durations=10
pytest --disable-warnings
```

---

# 🎯 Interview Tip

If you are working in Selenium + PyTest framework, the most commonly used commands are:

```bash
pytest -v
pytest -s
pytest -m smoke
pytest -m regression
pytest -n auto
pytest --html=report.html
pytest --junitxml=result.xml
pytest --reruns 2
pytest --lf
pytest --ff
```

These commands cover approximately 90% of real-world automation project executions.