import requests
import sys

api_url = "https://demo.defectdojo.org/api/v2"

auth_payload = {
  # Demo defect dojo username and password
  "username": "admin",
  "password": "1Defectdojo@demo#appsec"
}

file_name = sys.argv[1];

if file_name == "gitleaks.sarif":
  scan_type = "Gitleaks Scan"
elif file_name == "njsscan.sarif":
  scan_type = "njsscan Scan"
elif file_name == "semgrep.json":
  scan_type = "Semgrep JSON Report"
elif file_name == "retirejs.json":
  scan_type = "Retire.js Scan"

# response = requests.post(f"{api_url}/api-token-auth/", json=auth_payload)



# auth_token = f"Token {response.json()['token']}"

auth_token = "Token cce932d1884fd905f1c595740a5e0cfc15c64b35"

headers = {
  "Authorization": auth_token
}


files = {
  "file": open(file_name, "rb")
}

data = {
  "minimum_severity": "Low",
  "scan_type": scan_type,
  "active": "true",
  "verified": "true",
  "engagement": 28
}

upload_response = requests.post(url=f"{api_url}/import-scan/", headers=headers, data=data, files=files)

if upload_response.status_code == 201:
  print(f"{file_name} successfully uploaded")
else:
  print("There is some issue with the file uploading", upload_response.status_code, upload_response.json())
