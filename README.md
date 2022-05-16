# Apache Log Parser

## Introduction

This script fetches an Apache log file at `https://pastebin.com/gstGCJv4`, parses it then prints out a few facts about the data in the log file.

## Installation

This script uses a 3rd party library called [apachelogs](https://github.com/jwodder/apachelogs).

You can install it by running:

```pip3 install apachelogs```

or using the provided `requirements.txt` file:

```pip install -r requirements.txt```

## Usage

Run the script using:

```
python apache_log_analyzer.py
```

Expected output:

```console
How many times the URL "/production/file_metadata/modules/ssh/sshd_config" was fetched: 6
Of those requests, how many times the return code from Apache was not 200: 0
The total number of times Apache returned any code other than 200: 6
The total number of times that any IP address sent a PUT request to a path under "/dev/report/": 9
A breakdown of how many times such requests were made by IP address: 
  1 of those requests were made by 10.101.3.205
  1 of those requests were made by 10.114.199.41
  1 of those requests were made by 10.204.150.156
  1 of those requests were made by 10.204.211.99
  1 of those requests were made by 10.34.89.138
  13 of those requests were made by 10.39.111.203
  1 of those requests were made by 10.80.146.96
  1 of those requests were made by 10.80.174.42
  1 of those requests were made by 10.80.58.67

```
