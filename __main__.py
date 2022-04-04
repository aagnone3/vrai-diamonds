import json
import re
from typing import Any, Dict, List

import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    response = requests.get(url)
    if not response.ok:
        raise RuntimeError(f"{response.status_code} received: {response.text}")
    return response.text


def parse_diamond_data(html: str) -> List[Dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")

    script_id = "__NEXT_DATA__"
    script_tag = soup.find(id=script_id)
    if script_tag is None:
        raise RuntimeError(f"<script> tag with id #{script_id} not found in HTML")

    cleaned_text = re.sub(r"\s", "", script_tag.text)
    json_info = json.loads(cleaned_text)
    return json_info['props']['initialState']['data']

    
def main():
    # with open("etc/example_response.html", 'r') as fp:
    #     html = fp.read().strip()
    html= get_html("https://www.vrai.com/diamonds")

    diamonds_info = parse_diamond_data(html)
    with open("output.json", 'w') as fp:
        json.dump(diamonds_info, fp, indent=4)

    
if __name__ == '__main__':
    main()
