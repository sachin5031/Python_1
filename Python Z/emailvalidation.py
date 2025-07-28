def fun(s: str) -> bool:
    # Splitting the email into parts
    if "@" not in s:
        return False
    parts = s.split("@")
    if len(parts) != 2:
        return False

    username, rest = parts

    # Check if the username is valid
    if not username or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_." for c in username):
        return False

    # Splitting the remaining part
    if "." not in rest:
        return False
    domain_parts = rest.split(".")
    if len(domain_parts) != 2:
        return False

    websitename, extension = domain_parts

    # Check if the website name and extension are valid
    if not websitename or not all(c.isalnum() for c in websitename):
        return False
    if not extension or len(extension) > 3 or not all(c.isalpha() for c in extension):
        return False

    return True

def filter_emails(emails):
    # Filter and sort valid emails
    valid_emails = [email for email in emails if fun(email)]
    return sorted(valid_emails)

# Input reading and function execution
if __name__ == "__main__":
    n = int(input("Enter the number of email addresses: "))
    emails = [input("Enter email address: ") for _ in range(n)]
    result = filter_emails(emails)
    print("Valid email addresses in lexicographical order:")
    print(result)
