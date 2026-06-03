import pytest


# @pytest.mark.smoke
def test_login_feature():
    pass

# @pytest.mark.smoke
def test_notification_feature():
    assert False

@pytest.mark.skip(reason='under process test')
def test_payment_feature():
    pass

# if skip
@pytest.mark.skipif(not True, reason='under process test')
def test_order_placed_feature():
    pass
