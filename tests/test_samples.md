# Test Results
Python version used: 3.__ | Operating system: ________ | Date: ________
| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | | |
| 2 | http://192.0.2.10/account | IP address + HTTP | | |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | | |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | | |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | | |

##
I learned how to identify suspicious URLs and how Python can help raise awareness about phishing attacks. I was surprised that phishing links can look very similar to genuine websites, making them difficult to recognize.
##