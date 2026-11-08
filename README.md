# EWB Phishing URL Awareness Checker
## Overview
[2-3 sentences: what phishing is, and what your tool does.]
## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- [Your improvement 1]
- [Your improvement 2]
## Requirements
Python 3.10 or later. No extra packages.
## How to Run
Windows: python phishing_checker.py
Mac/Linux: python3 phishing_checker.py
## Example Output
[Paste the output of one run here.]
## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | [fill] | [PASS] |
[Add rows 2 to 5. Full table is in tests/test_samples.md]
## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_result.png)
## Improvements
1. [Name] - [what changed, why, how you tested it]
2. [Name] - [what changed, why, how you tested it]
## Limitations
This is an educational tool. It only reads URL text. It does not visit
URLs, scan for malware or prove that a URL is safe. No warning signs
found does NOT mean a URL is safe.
## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this
project to deceive anyone or to test websites without permission.
## Author
Sidharth Sahoo