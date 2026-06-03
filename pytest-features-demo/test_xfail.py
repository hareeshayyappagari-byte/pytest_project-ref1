""" xfail (Expected Failure) is used when you already know a test is going to
fail, but you still want it to be part of the test suite and reported separately.
"""


import pytest
# Syntax
@pytest.mark.xfail
def test_payment():
    assert False




# Real-Time Automation Scenarios
# 1. Known Bug Exists
#
# Suppose developers have already logged a defect:
#
# Bug ID: BUG-1234
#
# The login button doesn't work on Firefox.

import pytest

@pytest.mark.xfail(reason="BUG-1234: Login button not working on Firefox")
def test_login_firefox():
    assert True
#
# Why use xfail?
#
# Test remains in the suite.
# CI/CD pipeline doesn't fail because of a known issue.
# Team can track the failing test.


# 2. Feature Under Development
#
# The "Export to PDF" feature is not completed yet.

@pytest.mark.xfail(reason="Feature under development")
def test_export_pdf():
    pass





# 3. Third-Party Dependency Issue
#
# Your application depends on an external API that is currently unstable.

@pytest.mark.xfail(reason="External API issue")
def test_fetch_customer_data():
    assert True





# 4. Environment-Specific Issue
#
# Works in QA but fails in UAT due to a known configuration problem.

@pytest.mark.xfail(reason="Known UAT environment issue")
def test_email_notification():
    assert 'hari' == 'hari'



# 5. Temporary Failure During Migration
#
# During a database migration, some reports are expected to fail.

@pytest.mark.xfail(reason="DB migration in progress")
def test_generate_report():
    assert 2+2 == 5