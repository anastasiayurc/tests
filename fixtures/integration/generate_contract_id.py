import pytest


@pytest.fixture
def generate_contract_id(msdbconn):
    """
    This is an example fixture for how to generate test data for integration tests.

    There are two major parts:

    1. creation of the test data
    2. deletion of the test data

    Anything above the `yield` is where you should create your test data. Anything
    below the `yield` is where you should add your cleanup code.

    The example returns a contract ID that can be used in the test. Your test fixtures
    can return as much or as little data as you need (scalar values, dictionary, tuple,
    etc).
    :param msdbconn:
    :return:
    """
    msdbconn.execute(
        """
            INSERT INTO [merchants] (
                MerchantName,
                MerchantDBA
            ) VALUES (
                'Test Merchant 1 LLC',
                'Test Merchant 1'
            )
        """
    )
    merchant_id = msdbconn.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]

    msdbconn.execute(
        """
            INSERT INTO [contracts] (
                merchant_id,
                contractStatus_id
            ) VALUES (
                {0},
                1
            )
        """.format(merchant_id)
    )
    contract_id = msdbconn.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]
    msdbconn.commit()

    # The value(s) that your fixture will return
    yield contract_id

    # everything after here for cleanup
    msdbconn.execute("DELETE FROM [merchants] WHERE [id] = ?", merchant_id)
    msdbconn.execute("DELETE FROM [contracts] WHERE [id] = ?", contract_id)
    msdbconn.commit()
