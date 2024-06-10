from time import sleep

import botocore
import boto3
import json
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from retry.api import retry_call

UNDERWRITING_CASE_PREAPPROVAL_COMPLETED_CONTRACT_STATUS_ID = 14

UNDERWRITING_CASE_PENDregion = us-east-1ING_CONTRACT_STATUS_ID = 22

UNDERWRITING_CASE_DECLINED_CONTRACT_STATUS_ID = 7

DECISIONED_MANAGER_REVIEW_CONTRACT_STATUS_ID = 14

DECISIONED_PENDING_CONTRACT_STATUS_ID = 22

DECISIONED_DECLINED_CONTRACT_STATUS_ID = 7


def make_api_request(generate_contract_id, domain, expected_status_id):
    try:
        contract_id = generate_contract_id
        session_boto3 = boto3.Session()
        credentials = session_boto3.get_credentials()
        creds = credentials.get_frozen_credentials()
        url = '{}/contracts/{}/status'.format(domain, contract_id)
        request = AWSRequest(method='GET', url=url)
        SigV4Auth(creds, 'execute-api', "us-east-1").add_auth(request)
        sleep(10)
        session_botocore = botocore.httpsession.URLLib3Session()
        response_session = session_botocore.send(request.prepare())
        response = json.loads(response_session.text)
        if 'contractStatus_id' not in response:
            print('contractStatus_id is not in the response: {}'.format(response))
            raise Exception("Error occurred")
        else:
            assert response['contractStatus_id'] == expected_status_id
    except botocore.exceptions.BotoCoreError as e:
        print(f"Error making API request: {e}")
        raise Exception("Unable to make API request")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")
        raise Exception("Unable to send request")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e


def send_event(event):
    eventbridge_client = boto3.client('events', region_name='us-east-1')
    # send a raw event to EventBridge to trigger the rule
    return eventbridge_client.put_events(
        Entries=[event]
    )


class TestEventRouting:
    """
    Contains Integration tests related to our service responding to the events we expect in the way we expect
    """

    def test_platform_contract_status_api_invoked_on_backbase_decisioned_declined(self, get_decisioned_declined_event,
                                                                                  generate_contract_id, invoke_url,
                                                                                  event_bus_name, account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'DECISIONED_DECLINED', and is in
        the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status` endpoint
        with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        event = get_decisioned_declined_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, sign the requests to the API using signv4 auth
        retry_call(make_api_request, fargs=[contract_id, invoke_url, DECISIONED_DECLINED_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))

    def test_platform_contract_status_api_invoked_on_backbase_decisioned_pending(self, get_decisioned_pending_event,
                                                                                 generate_contract_id, invoke_url,
                                                                                 event_bus_name, account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'DECISIONED_PENDING', and is in
        the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status` endpoint
        with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        event = get_decisioned_pending_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, sign the requests to the API using signv4 auth
        retry_call(make_api_request, fargs=[contract_id, invoke_url, DECISIONED_PENDING_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))

    def test_platform_contract_status_api_invoked_on_backbase_decisioned_manager_review(self,
                                                                                        get_decisioned_manager_review_event,
                                                                                        generate_contract_id,
                                                                                        invoke_url,
                                                                                        event_bus_name, account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'DECISIONED_DECLINED', and is in
        the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status` endpoint
        with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        event = get_decisioned_manager_review_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, sign the requests to the API using signv4 auth
        retry_call(make_api_request, fargs=[contract_id, invoke_url, DECISIONED_MANAGER_REVIEW_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))

    def test_platform_contract_status_api_invoked_on_backbase_underwriting_case_declined(self,
                                                                                         get_underwriting_case_declined_event,
                                                                                         generate_contract_id,
                                                                                         invoke_url,
                                                                                         event_bus_name, account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'underwriting_case_declined', and is in
        the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status` endpoint
        with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        event = get_underwriting_case_declined_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, signs the requests to the API using sigv4 auth
        retry_call(make_api_request, fargs=[contract_id, invoke_url, UNDERWRITING_CASE_DECLINED_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))

    def test_platform_contract_status_api_invoked_on_backbase_underwriting_case_pending(self,
                                                                                        get_underwriting_case_pending_event,
                                                                                        generate_contract_id,
                                                                                        invoke_url,
                                                                                        event_bus_name, account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'underwriting_case_pending', and is in
        the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status` endpoint
        with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        event = get_underwriting_case_pending_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, signs the requests to the API using sigv4 auth
        retry_call(make_api_request, fargs=[contract_id, invoke_url, UNDERWRITING_CASE_PENDING_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))

    def test_platform_contract_status_api_invoked_on_backbase_underwriting_case_preapproval_completed(self,
                                                                                                      get_underwriting_case_preapproval_completed_event,
                                                                                                      generate_contract_id,
                                                                                                      invoke_url,
                                                                                                      event_bus_name,
                                                                                                      account_id):
        """
        Given an event on the event bus we listen to comes from Backbase, is of type 'underwriting_case_preapproval_completed, and is
        in the format defined in the event schema, we expect to invoke the Platform's `POST /api/contract/status`
        endpoint with the correct payload.
        :return:
        """
        # get contract_id from fixture
        contract_id = generate_contract_id
        # send a raw event to EventBridge to trigger the rule
        event = get_underwriting_case_preapproval_completed_event(contract_id, event_bus_name, account_id)
        event_response = send_event(event)
        # check if the event was successfully put to EventBridge
        assert event_response['FailedEntryCount'] == 0
        # invoke your endpoint, signs the requests to the API using sigv4 auth
        retry_call(make_api_request,
                   fargs=[contract_id, invoke_url, UNDERWRITING_CASE_PREAPPROVAL_COMPLETED_CONTRACT_STATUS_ID],
                   exceptions=AssertionError, tries=3, delay=5, jitter=(1, 1.1))
