import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return["No URL entered"]

    candidate = url if "://" in url else "http://" + url
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except Exception:
        raise ValueError("The URL format could not be parsed: " + url)

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully")

    if len(url) > 100:
        findings.append("Unusually long URL (Over 100 charecters).")
    
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses IP address instead of a fimiliar domain")
    
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
    
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
    
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone doesnot proves truest.")

    if not findings:
        findings.append("No listed warning signs found . this does Not prove safety.")

    return findings

def main():
    print("EWB Phising URL Awareness Checker")
    print("Text checks only - this program does not opens URLs.")
    print("Developed by Sidharth Sahoo")
    print("Type 'q', 'quit', or 'exit' to stop.\n")

    while True:
        raw_url = input("Enter a sample URL to inspect: ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        try:
            findings = inspect_url(raw_url)
        except Exception as e:
            print("- Malformed URL: could not parse (" + str(e) + ")")
            print()
            continue

        # Count findings that are actual warnings (not the "no warnings" message)
        warnings = [f for f in findings if not f.startswith("No listed warning signs")]
        warning_count = len(warnings)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        if warning_count > 0:
            print("\n⚠  REVIEW CAREFULLY – " + str(warning_count) + " warning sign(s) found.")

        print("\nNever enter passwords from unexpected links.\n")

if __name__ == "__main__":
    main()