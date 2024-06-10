import json
import pytest


@pytest.fixture
def get_decisioned_pending_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "Source": "Test",
            "DetailType": "DECISIONED_PENDING",
            "Detail": json.dumps({
                "schema": {
                    "type": "test",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "ab90775d-e7c2-4589-a406-ddc7f4f86c37",
                            "businessId": "1450041",
                            "offerId": "599025",
                            "contractId": int(contract_id),
                            "caseDecisionReasons": [
                                "Additional Information Requested - Stips",
                                "Locked Credit",
                                "Offer Selected - Checkout Process Pending",
                                "Data Error-Technical Issue",
                                "Offer Sent"
                            ]
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "e4d87374-22a0-4fda-bacc-03aa0643f219",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiZTRkODczNzQtMjJhMC00ZmRhLWJhY2MtMDNhYTA2NDNmMjE5IiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0wOFQxNDoxOTozNVoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-08T14:19:35Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "test",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event


@pytest.fixture
def get_decisioned_declined_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "DetailType": "DECISIONED_DECLINED",
            "Source": "test",
            "Detail": json.dumps({
                "schema": {
                    "type": "test",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "event": {
                    "id": "a1eaf774-7170-4dc1-8221-a19d66afaa2a",
                    "idempotency-key": "4d700953-87f2-4430-98ea-c5765c3375ba",
                    "message-scope": 0,
                    "timestamp": "2023-12-08T14:19:35Z"
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "199f89e1-6fb7-4aae-8089-be752e83a770",
                            "businessId": "1722521",
                            "offerId": "659831",
                            "contractId": int(contract_id),
                            "declineReasons": [
                                {
                                    "category": "Insufficient/Inconsistent Cashflow",
                                    "reason": "Inconsistent volume",
                                    "reasonId": 7
                                }
                            ],
                            "kapitusPaymentMethod": "ACH Transfer",
                            "merchantDebitDate": "2023-06-30"
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "5ecc10fa-269c-4d8e-a170-7c5e6422aa7c",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiNWVjYzEwZmEtMjY5Yy00ZDhlLWExNzAtN2M1ZTY0MjJhYTdjIiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0xMVQxMjozNjo0NFoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-11T12:36:44Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "test",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event


@pytest.fixture()
def get_decisioned_manager_review_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "Source": "test",
            "DetailType": "DECISIONED_MANAGER_REVIEW",
            "Detail": json.dumps({
                "schema": {
                    "type": "test",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "65f6ad8d-076d-46f9-b0cd-218e6667a373",
                            "businessId": "1624521",
                            "offerId": "679801",
                            "contractId": int(contract_id),
                            "kapitusPaymentMethod": "Wire Transfer",
                            "merchantDebitDate": "2023-08-10"
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "3a5e2395-485a-4161-9b26-bd0180d208b4",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiM2E1ZTIzOTUtNDg1YS00MTYxLTliMjYtYmQwMTgwZDIwOGI0IiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0xMVQxMDowNjozNFoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-11T10:06:34Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "test",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event


@pytest.fixture
def get_underwriting_case_pending_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "Source": "com.test",
            "DetailType": "underwriting_case_pending",
            "Detail": json.dumps({
                "schema": {
                    "type": "test",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "ab90775d-e7c2-4589-a406-ddc7f4f86c37",
                            "businessId": "1450041",
                            "offerId": "599025",
                            "contractId": int(contract_id),
                            "caseDecisionReasons": [
                                "Additional Information Requested - Stips",
                                "Locked Credit",
                                "Offer Selected - Checkout Process Pending",
                                "Data Error-Technical Issue",
                                "Offer Sent"
                            ]
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "e4d87374-22a0-4fda-bacc-03aa0643f219",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiZTRkODczNzQtMjJhMC00ZmRhLWJhY2MtMDNhYTA2NDNmMjE5IiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0wOFQxNDoxOTozNVoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-08T14:19:35Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "Backbase",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event


@pytest.fixture
def get_underwriting_case_declined_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "DetailType": "underwriting_case_declined",
            "Source": "com.test",
            "Detail": json.dumps({
                "schema": {
                    "type": "tets",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "event": {
                    "id": "a1eaf774-7170-4dc1-8221-a19d66afaa2a",
                    "idempotency-key": "4d700953-87f2-4430-98ea-c5765c3375ba",
                    "message-scope": 0,
                    "timestamp": "2023-12-08T14:19:35Z"
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "199f89e1-6fb7-4aae-8089-be752e83a770",
                            "businessId": "1722521",
                            "offerId": "659831",
                            "contractId": int(contract_id),
                            "declineReasons": [
                                {
                                    "category": "Insufficient/Inconsistent Cashflow",
                                    "reason": "Inconsistent volume",
                                    "reasonId": 7
                                }
                            ],
                            "kapitusPaymentMethod": "ACH Transfer",
                            "merchantDebitDate": "2023-06-30"
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "5ecc10fa-269c-4d8e-a170-7c5e6422aa7c",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiNWVjYzEwZmEtMjY5Yy00ZDhlLWExNzAtN2M1ZTY0MjJhYTdjIiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0xMVQxMjozNjo0NFoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-11T12:36:44Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "test",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event


@pytest.fixture()
def get_underwriting_case_preapproval_completed_event():
    def get_event(contract_id, event_bus_name, account_id):
        return {
            "Source": "com.test",
            "DetailType": "underwriting_case_preapproval_completed",
            "Detail": json.dumps({
                "schema": {
                    "type": "test",
                    "version": "1",
                    "schema-url": "arn:aws:schemas:us-east-1:{}:schema/mercury-schema-registry/test".format(account_id)
                },
                "message": {
                    "type": "STATE-CHANGE",
                    "description": "A sample event for testing purposes for platform-api-gate.",
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "payload": {
                        "details": {
                            "caseId": "65f6ad8d-076d-46f9-b0cd-218e6667a373",
                            "businessId": "1624521",
                            "offerId": "679801",
                            "contractId": int(contract_id),
                            "kapitusPaymentMethod": "Wire Transfer",
                            "merchantDebitDate": "2023-08-10"
                        }
                    },
                    "tags": []
                },
                "parent-process": {
                    "state": {
                        "success": True,
                        "warning": False
                    },
                    "elapsed-time": 0,
                    "process-id": "3a5e2395-485a-4161-9b26-bd0180d208b4",
                    "process-descriptor": "Job: STATE-CHANGE",
                    "parent-process-token": "eyJzdGF0ZSI6IHsic3VjY2VzcyI6IHRydWUsICJ3YXJuaW5nIjogZmFsc2UsICJkZXRhaWxzIjogbnVsbH0sICJlbGFwc2VkX3RpbWUiOiAwLjAsICJsYXN0X2V2ZW50X2lkIjogbnVsbCwgInByb2Nlc3NfaWQiOiAiM2E1ZTIzOTUtNDg1YS00MTYxLTliMjYtYmQwMTgwZDIwOGI0IiwgInByb2Nlc3NfZGVzY3JpcHRvciI6ICJKb2I6IFNUQVRFLUNIQU5HRSIsICJwcm9jZXNzX2tleSI6IG51bGwsICJwYXJlbnRfcHJvY2Vzc190b2tlbiI6IG51bGwsICJwcm9jZXNzX3N0YXJ0X3RpbWUiOiAiMjAyMy0xMi0xMVQxMDowNjozNFoiLCAicHJvY2Vzc19lbmRfdGltZSI6IG51bGwsICJleGVjdXRpb25fc3RhdHVzIjogIlJVTk5JTkcifQ==",
                    "process-start-time": "2023-12-11T10:06:34Z",
                    "execution-status": "RUNNING"
                },
                "producer": {
                    "name": "test",
                    "type": "SERVICE"
                }
            }),
            "EventBusName": event_bus_name
        }
    return get_event
