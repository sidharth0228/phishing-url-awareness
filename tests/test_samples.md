# Test Results

**Python version:** 3.9.6 | **Operating system:** macOS | **Date:** 2026-11-08

## Original five test cases (Part 08)

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove the URL is safe – always verify the source. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain name. / Uses HTTP – the connection is not encrypted. ⚠ REVIEW CAREFULLY – 2 warning sign(s) found. | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol – the part before @ may not be the real site. / Uses HTTP – the connection is not encrypted. ⚠ REVIEW CAREFULLY – 2 warning sign(s) found. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments / subdomains. ⚠ REVIEW CAREFULLY – 1 warning sign(s) found. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname (xn--). ⚠ REVIEW CAREFULLY – 1 warning sign(s) found. | PASS |

## Part 10 improvement test cases

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 6 | *(empty)* | No crash; clear message | No URL entered. Please type a URL and press Enter. | PASS |
| 7 | `not_a_valid_url` | No crash; handled gracefully | HTTP warning shown; program continues. | PASS |
| 8 | Two URLs in sequence | Loop continues after each | Both URLs inspected; loop did not exit early. | PASS |
| 9 | `q` | Program exits cleanly | Goodbye! Stay safe online. | PASS |

---

## Reflection

I learned how to identify suspicious URLs and how Python can help raise awareness about phishing
attacks. I was surprised that phishing links can look very similar to genuine websites, making them
difficult to recognise. The project also taught me how to handle unexpected user input gracefully
using try-except, and how to structure a loop-based program that keeps running until the user
decides to quit.
