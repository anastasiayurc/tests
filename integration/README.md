# Integration Tests

Currently, the integration tests rely on direct access to the database Platform uses as its system of record. This is 
not ideal, but it is the best we can do for now.

In the future we might want to leverage APIs (or different data sources) in order to set up the data required, so with
this in mind the fixtures for the tests should be decoupled from the tests themselves. In other words, the way the data
is set up should be decoupled from the tests that use it.

This is the design philosophy for these tests


## Running the tests

To run the tests:

1. `pip install -r requirements.txt`
2. ```
    python -m pytest tests/integration --ms-db-host <hostname for database being used> \
                                   --ms-db-name <database name> \
                                   --ms-db-user <username for db> \
                                   --ms-db-pass <password for db> \
                                   --invoke-url <api invoke url for dev, prod-mirror or prod> \
   ```
3. Parameter invoke url can be for dev, prod-mirror or prod, e.g for prod-mirror: --invoke-url https://test.com

## Creating Fixtures

All the fixtures for the integration tests should be located in `tests/fixtures/integration`. One file per fixture. 
It's not enough for the file to  just be placed here though, there are a few steps involved in creating a fixture:

1. Create the file(s) in the correct location: `tests/fixtures/integration`
   1. For each function in there
      1. Create your data at the top
      2. `yield` to return the data
      3. Clean up the data at the bottom
2. Edit `tests/integration/conftest.py`:
   1. Add an entry to `pytest_plugins` for the new fixture file. For example: `tests.fixtures.integration.<fixture_file_name>`
   
See `tests/fixtures/integration/generate_contract_example.py` for an example of a fixture 
file. 
See `tests/integration/conftest.py` for an example of it being made available for use. 
See