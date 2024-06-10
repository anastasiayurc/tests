import pytest
import pyodbc


_integration_test_settings = {}

pytest_plugins = [
    "tests.fixtures.integration.generate_contract_id",
    "tests.fixtures.integration.events"
]


def pytest_addoption(parser):
    parser.addoption("--ms-db-host", action="store", help="host for the mssql server used in testing to create test data")
    parser.addoption("--ms-db-name", action="store", help="name of the database in mssql. usually SFSDB")
    parser.addoption("--ms-db-user", action="store", help="username for the mssql server")
    parser.addoption("--ms-db-pass", action="store", help="password for the mssql server")
    parser.addoption("--invoke-url", action="store", help="api invoke url for dev, prod-mirror or prod")
    parser.addoption("--event-bus-name", action="store", help="event bus name where to put the events")
    parser.addoption("--account-id", action="store", help="AWS account id e.g. for DEV account id is 127023561800")


def pytest_configure(config: pytest.Config):
    # configure the database connection for the msdbconn fixture
    global _integration_test_settings
    _integration_test_settings = {
        'driver': '{ODBC Driver 18 for SQL Server}',
        'host': config.getoption("--ms-db-host"),
        'user': config.getoption("--ms-db-user"),
        'password': config.getoption("--ms-db-pass"),
        'database': config.getoption("--ms-db-name"),
        'TrustServerCertificate': 'Yes',
        'invokeUrl': config.getoption("--invoke-url"),
        'eventBusName': config.getoption("--event-bus-name"),
        'accountId': config.getoption("--account-id")
    }


@pytest.fixture(scope="session")
def invoke_url():
    global _integration_test_settings
    if _integration_test_settings.get('invokeUrl') is None:
        raise pytest.UsageError(
            "Integration test settings not configured. Provide --invoke-url?"
        )
    return _integration_test_settings.get('invokeUrl')


@pytest.fixture(scope="session")
def event_bus_name():
    global _integration_test_settings
    if _integration_test_settings.get('eventBusName') is None:
        raise pytest.UsageError(
            "Integration test settings not configured. Provide --event-bus-name"
        )
    return _integration_test_settings.get('eventBusName')


@pytest.fixture(scope="session")
def account_id():
    global _integration_test_settings
    if _integration_test_settings.get('accountId') is None:
        raise pytest.UsageError(
            "Integration test settings not configured. Provide --account-id"
        )
    return _integration_test_settings.get('accountId')


@pytest.fixture(scope="session")
def msdbconn() -> pyodbc.Connection:
    """
    Returns a connection to the MS SQL database used for integration testing
    :return:
    """
    global _integration_test_settings
    if len(_integration_test_settings) == 0:
        raise pytest.UsageError(
            "Integration test settings not configured. Did `pytest_configure` run?"
        )
    else:
        return pyodbc.connect(
            **_integration_test_settings
        )
