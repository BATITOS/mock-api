# Test Plan – Mock API Service
    
## Overview
    This test plan describes the testing strategy for the Mock API Service.
    The purpose of testing is to verify the API correctly handles valid and invalid requests and returns appropriate HTTP status codes.
    Testing will include both manual checks (Postman) and automated tests (Pytest).
    
## Test Objectives
    - Verify the API returns HTTP 200 for valid requests.
    - Verify the API returns HTTP 400 for invalid input.
    - Verify the API returns HTTP 500 for server errors.
    - Ensure responses are consistent and predictable.

## Scope
### In Scope
    - API endpoint behavior (sending requests and validating responses).
    - Input validation.
    - HTTP status codes (200,400,500).
    
### Out of Scope
    - Performance and load testing.
    - Security testing (has no security layer).
    - UI testing (no frontend in this project).
    - Database testing (no database in this project).
    
## Test Approach
    Testing will be preformed using a combination of manual and automated methods:
    - Manual testing will be preformed by Postman to send HTTP requests and verify responses.
    - Automated testing will be implemented using Pytest to validate API behavior.
    - Tests will cover both positive and negative scenarios (valid / invalid inputs).
    - The Mock API will run inside a Docker container during testing.
    - Automated tests will be executed as part of the CI/CD pipeline to ensure consistent results.

## Test Scenarios
| Test Case ID | Scenario Description | Input | Output | Expected Result |
|-------------|----------------------|-------|--------|----------------|
| TC-01 | Send a valid request | Valid JSON with all required fields | Valid JSON response | HTTP 200 OK |
| TC-02 | Missing required field | JSON missing one required field | Error message in JSON | HTTP 400 Bad Request |
| TC-03 | Invalid data type | Field with incorrect data type | Error message in JSON | HTTP 400 Bad Request |
| TC-04 | Malformed JSON | Invalid JSON format | Error message in JSON | HTTP 400 Bad Request |
| TC-05 | Simulated server error | Request to /error endpoint | Error response | HTTP 500 Internal Server Error |

## Test Environment
    - OS: Linux (Docker container)
    - Programming Language: Python
    - Frameworks/Libraries:
        - FastAPI (Mock API implementation).
        - Pytest (automated testing).
    - Tools:
        - Docker.
        - Jenkins (CI/CD execution).
        - Postman.
    
## Success Criteria
    Testing will be successful if:
    - All planned test scenarios have been executed.
    - All critical test cases pass successfully.
    - The API consistently returns the correct HTTP status code for the tested scenario.
    - Automated tests pass successfully in the CI/CD pipeline.