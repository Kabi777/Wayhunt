import requests
import os
import sys

# Banner
print("""
«==========================================»
          Wayhunt - Archive Scraper
«==========================================»
      A tool for scraping and categorizing
      URLs from the Wayback Machine!
-------------------------------------------
                 by kabi_777
«==========================================»
""")

if len(sys.argv) != 2:
    print("Usage: python script.py <target_domain>")
    sys.exit(1)

# Target domain
TARGET = sys.argv[1]

# Step 1: Fetch links from the Wayback Machine
print(f"Step 1: Fetching URLs for the domain {TARGET} from the Wayback Machine...")
response = requests.get(f"https://web.archive.org/cdx/search/cdx",
                        params={"url": f"*.{TARGET}/*", "collapse": "urlkey",
                                "output": "text", "fl": "original"})

if response.status_code == 200:
    print("URLs fetched successfully.")
else:
    print(f"Failed to fetch URLs. HTTP Status Code: {response.status_code}")
    sys.exit(1)

# Step 2: Save the URLs to a file
print(f"Step 2: Saving the URLs to {TARGET}/urls.txt...")
os.makedirs(TARGET, exist_ok=True)
with open(f"{TARGET}/urls.txt", "w") as file:
    file.write(response.text)

print(f"URLs saved to {TARGET}/urls.txt.")

# Step 3: Create categorized_files folder
print(f"Step 3: Creating folder for categorized files...")
os.makedirs(f"{TARGET}/categorized_files", exist_ok=True)

# Step 4: List of file extensions to filter
print("Step 4: Preparing list of file extensions for categorization...")

extensions = [
    "xls", "xml", "xlsx", "json", "pdf", "sql", "doc", "docx",
    "pptx", "txt", "zip", "tar.gz", "tgz", "bak", "7z", "rar",
    "log", "cache", "secret", "db", "backup", "yml", "gz", "config",
    "csv", "yaml", "md", "md5", "exe", "dll", "bin", "ini", "bat",
    "sh", "tar", "deb", "rpm", "iso", "img", "apk", "msi", "dmg",
    "tmp", "crt", "pem", "key", "pub", "asc", "xls", "js", "jpg",
    "jpeg", "svg", "png", "img"
]

# Step 5: Create a file to save URLs with parameters
print(f"Step 5: Creating file for URLs with parameters...")
with open(f"{TARGET}/categorized_files/urls_with_parameters.txt", "w") as param_file:
    # Categorize the URLs and save them based on the file extension
    print("Step 6: Categorizing URLs...")
    with open(f"{TARGET}/urls.txt", "r") as file:
        for url in file:
            clean_url = url.strip()
            if '?' in clean_url:  # Check if the URL contains parameters
                param_file.write(clean_url + "\n")

            file_name = clean_url.split('/')[-1]  # Extract the file name
            extension = file_name.split('.')[-1] if '.' in file_name else None

            # Check if the extension is in the allowed list
            if extension and extension in extensions:
                with open(f"{TARGET}/categorized_files/{extension}_files.txt", "a") as ext_file:
                    ext_file.write(clean_url + "\n")

print(f"Step 7: URLs have been categorized and saved in the '{TARGET}/categorized_files' folder!")

print("Script completed successfully!")
