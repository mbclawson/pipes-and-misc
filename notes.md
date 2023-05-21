## Notes
To activate the dp venv, run `source ../environments/dp/Scripts/activate`

## GitBash
~ is a user's home directory.  

## Extracting Data from a REST API
Definitions
- Application Programming Interface (API): set of rules that define how applications or devices can connect to and communicate with each other
- Representational State Transfer Architectural Style (REST): REST is a set of rules/standards/guidelines for how to build a web API.  Not all APIs are REST, however all REST services are APIs

Pattern for data extraction
1. Send an HTTP GET request to API endpoint
2. Accept the response (most likely formatted in JSON)
3. Parse response and 'flatten' it into a CSV (for later loading)
