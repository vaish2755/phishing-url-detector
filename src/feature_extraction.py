import re
from urllib.parse import urlparse


def extract_features(url):
    """
    Extract lexical features from a URL.
    The leading 'www.' is normalized so that it does not
    unnecessarily affect lexical features.
    """

    features = {}

    # --------------------------------------------------
    # Normalize URL
    # --------------------------------------------------

    url = url.strip()

    # Remove leading www. after http:// or https://
    normalized_url = re.sub(
        r"^(https?://)www\.",
        r"\1",
        url,
        flags=re.IGNORECASE
    )

    # Use normalized URL for lexical features
    url_for_features = normalized_url

    # --------------------------------------------------
    # Basic URL features
    # --------------------------------------------------

    features["url_length"] = len(url_for_features)

    features["dot_count"] = url_for_features.count(".")

    features["slash_count"] = url_for_features.count("/")

    features["hyphen_count"] = url_for_features.count("-")

    features["digit_count"] = sum(
        char.isdigit()
        for char in url_for_features
    )

    # --------------------------------------------------
    # Special characters
    # --------------------------------------------------

    special_characters = "@?=&%_~"

    features["special_char_count"] = sum(
        url_for_features.count(char)
        for char in special_characters
    )

    # --------------------------------------------------
    # @ symbol
    # --------------------------------------------------

    features["has_at_symbol"] = int(
        "@" in url_for_features
    )

    # --------------------------------------------------
    # Parse hostname
    # --------------------------------------------------

    try:
        parsed_url = urlparse(url_for_features)
        hostname = parsed_url.hostname or ""

    except ValueError:
        hostname = ""

    # --------------------------------------------------
    # IP address
    # --------------------------------------------------

    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    features["has_ip_address"] = int(
        bool(re.match(ip_pattern, hostname))
    )

    # --------------------------------------------------
    # Subdomain count
    # --------------------------------------------------

    if hostname:

        parts = hostname.split(".")

        features["subdomain_count"] = max(
            len(parts) - 2,
            0
        )

    else:

        features["subdomain_count"] = 0

    # --------------------------------------------------
    # Suspicious keywords
    # --------------------------------------------------

    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "password",
        "signin"
    ]

    url_lower = url_for_features.lower()

    features["has_suspicious_keyword"] = int(
        any(
            keyword in url_lower
            for keyword in suspicious_keywords
        )
    )

    return features


# ------------------------------------------------------
# Test
# ------------------------------------------------------

if __name__ == "__main__":

    test_urls = [
        "https://github.com",
        "https://www.github.com"
    ]

    for url in test_urls:

        print("\n" + "=" * 50)

        print("URL:", url)

        features = extract_features(url)

        for feature, value in features.items():

            print(f"{feature}: {value}")