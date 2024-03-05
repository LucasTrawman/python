import re
url = input("URL: ").strip()

username = re.sub(r"^https?://(?:www\.)?twitter\.com/", "", url) # It'll subtitute the first parameter with the second one on the 3rd parameter
print(f"Username: {username}")

################################################################

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE): # := makes an assignment value and comparison
    print(f"Username:{matches.group(1)}")
            
