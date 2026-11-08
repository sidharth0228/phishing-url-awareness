import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for phishing warning signs.

    Returns a list of finding strings.
    An empty list is never returned – either warnings or a clean message.
    """
    url = raw_url.strip()
    findings = []

    # Handle blank input before any parsing
    if not url:
        return ["No URL entered. Please type a URL and press Enter."]

    # Prepend a scheme if the user omitted it so urlparse can read the hostname
    candidate = url if "://" in url else "http://" + url

    # Catch any parsing errors from badly formed strings
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except Exception:
        raise ValueError("The URL could not be parsed. Check the format and try again.")

    # A missing hostname means nothing useful can be checked
    if not host:
        return ["Could not identify a hostname in the URL."]

    # A real hostname must contain at least one dot (e.g. example.com).
    # Single-label strings like 'hello' or 'not_a_valid_url' are not valid URLs.
    if "." not in host:
        return ["This does not look like a valid URL (no domain found)."]

    # --- Six original detection checks (preserved exactly) ---

    # Check 1: @ symbol (can hide the real destination)
    if "@" in candidate:
        findings.append("Contains an @ symbol – the part before @ may not be the real site.")

    # Check 2: Unusually long URL (common in obfuscation)
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check 3: Raw IP address instead of a domain name
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain name.")

    # Check 4: Many subdomains / hostname segments (5 or more labels)
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments / subdomains.")

    # Check 5: Punycode-style hostname (can disguise look-alike characters)
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname (xn--).")

    # Check 6: Plain HTTP (unencrypted connection)
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP – the connection is not encrypted.")

    # If none of the checks fired, report clean (but remind the user this is not a guarantee)
    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove the URL is safe – always verify the source."
        )

    return findings


def main():
    # --- Header ---
    print("=" * 55)
    print("  EWB Phishing URL Awareness Checker")
    print("  Text-based checks only – no URLs are opened.")
    print("  Developed by Sidharth Sahoo")
    print("=" * 55)
    print("Type  q / quit / exit  to stop.\n")

    while True:
        raw_url = input("Enter a URL to inspect: ").strip()

        # Quit keywords
        if raw_url.lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay safe online.")
            break

        # Run checks – catch any parse errors gracefully
        try:
            findings = inspect_url(raw_url)
        except ValueError as e:
            print(f"\n  Error: {e}\n")
            continue

        # Separate real warnings from informational messages
        # (empty-input, no-hostname, and no-warnings messages are not phishing warnings)
        SKIP_PREFIXES = (
            "No URL entered",
            "Could not identify",
            "No listed warning",
            "This does not look",
        )
        warnings = [f for f in findings if not any(f.startswith(p) for p in SKIP_PREFIXES)]
        warning_count = len(warnings)

        # --- Results ---
        print("\n" + "-" * 55)
        print("  Results")
        print("-" * 55)
        for item in findings:
            print(f"  - {item}")

        if warning_count > 0:
            print("-" * 55)
            print(f"  ⚠  REVIEW CAREFULLY – {warning_count} warning sign(s) found.")

        print("-" * 55)
        print("  Reminder: Never enter passwords from unexpected links.")
        print("-" * 55 + "\n")


if __name__ == "__main__":
    main()
