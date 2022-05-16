import re
from itertools import groupby
import urllib.request

from apachelogs import LogParser


def main():
    # Fetch log file
    print("Fetching log file...")
    response = urllib.request.urlopen("https://pastebin.com/raw/gstGCJv4")
    response_text = response.read().decode()

    # Parse log file
    parser = LogParser("%h %l %u %t \"%m %U%q %H\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    entries = [entry for entry in parser.parse_lines(response_text.split("\n"))]

    # Gather data about log file
    sshd_config = [e for e in entries if e.request_uri == "/production/file_metadata/modules/ssh/sshd_config"]
    sshd_config_nok = [e for e in sshd_config if e.final_status != 200]
    total_status_nok = [e for e in entries if e.final_status != 200]

    put_report_pattern = "^/dev/report/.*"
    put_report = [e for e in entries if re.findall(put_report_pattern, e.request_uri) and e.request_method == "PUT"]

    # Print results
    print(f'How many times the URL "/production/file_metadata/modules/ssh/sshd_config" was fetched: {len(sshd_config)}')
    print(f'Of those requests, how many times the return code from Apache was not 200: {len(sshd_config_nok)}')
    print(f'The total number of times Apache returned any code other than 200: {len(total_status_nok)}')
    print(f'The total number of times that any IP address sent a PUT request to a path under "/dev/report/": {len(put_report)}')
    print(f'A breakdown of how many times such requests were made by IP address: ')

    for k, g in groupby(sorted([e.remote_host for e in sshd_config + sshd_config_nok + total_status_nok + put_report])):
        print(f"  {len(list(g))} of those requests were made by {k}")


if __name__ == "__main__":
    main()
