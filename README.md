# Wayhunt - Archive Scraper

Wayhunt is a simple tool that scrapes URLs from the Wayback Machine (Internet Archive) and categorizes them based on their file extensions.

## Features

- Scrapes URLs related to a specified domain from the Wayback Machine.
- Categorizes URLs based on their file extensions (e.g., pdf, zip, json, etc.).
- Saves the categorized URLs in specific files for each extension.


## Installation
To use Wayhunt, follow these steps:

```
git clone https://github.com/Kabi777/Wayhunt

```
 **Navigate to the project folder**:
```
cd Wayhunt
chmod +x wayhunt.py
```
Now, you are ready to use Wayhunt!


## Usage
 
-To use Wayhunt, run the script from the command line as follows:

```bash
python3 wayhunt.py <target_domain>
```
- For example:
```
python3 wayhunt.py example.com
```
This will fetch URLs related to example.com from the Wayback Machine, categorize them by file type, and save the results in a folder named after the domain.

---
## Directory Structure

After running the script, the following directory structure will be created:
```
<target_domain>/
    ├── urls.txt            # Raw list of URLs scraped from the Wayback Machine
    └── categorized_files/
        ├── pdf_files.txt   # PDF URLs
        ├── json_files.txt  # JSON URLs
        └── ...             # Other categorized files
```
--- 
File Extensions Supported

Wayhunt supports categorizing the following file extensions:
```
xls, xml, xlsx, json, pdf, sql, doc, docx, pptx, txt, zip, tar.gz, tgz, bak, 7z, rar,
log, cache, secret, db, backup, yml, gz, config, csv, yaml, md, md5, exe, dll, bin, ini, 
bat, sh, tar, deb, rpm, iso, img, apk, msi, dmg, tmp, crt, pem, key, pub, asc, js, jpg, 
jpeg, svg, png
```
## Acknowledgements

Some parts of this project were inspired by or taken from the work of **LostSec**. We would like to thank them for their contributions and share their knowledge. 
 [LostSec GitHub](https://github.com/coffinxp)

