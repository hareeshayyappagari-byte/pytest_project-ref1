import pytest


@pytest.mark.smoke
def test_login():
    pass

@pytest.mark.smoke
def test_invalid_login():
    assert False

@pytest.mark.regression
def test_place_order():
    pass

@pytest.mark.payment
def test_upi_payment():
    pass

@pytest.mark.api
def test_get_user_details():
    pass


@pytest.mark.sanity
def test_user_can_login():
    pass

@pytest.mark.sanity
def test_user_can_logout():
    pass

@pytest.mark.sanity
def test_create_new_order():
    pass

@pytest.mark.sanity
def test_search_product():
    pass

@pytest.mark.sanity
def test_recent_bug_fix_for_payment():
    pass

@pytest.mark.login
def test_valid_login():
    pass

@pytest.mark.login
def test_invalid_password():
    pass

@pytest.mark.login
def test_invalid_username():
    pass

@pytest.mark.login
def test_blank_username():
    pass

@pytest.mark.login
def test_blank_password():
    pass

@pytest.mark.login
def test_forgot_password():
    pass

@pytest.mark.login
def test_account_lock_after_multiple_failures():
    pass


@pytest.mark.signup
def test_successful_registration():
    pass

@pytest.mark.signup
def test_registration_with_existing_email():
    pass

@pytest.mark.signup
def test_invalid_email_format():
    pass

@pytest.mark.signup
def test_password_policy_validation():
    pass

@pytest.mark.signup
def test_mandatory_fields_validation():
    pass

@pytest.mark.signup
def test_email_verification():
    pass


