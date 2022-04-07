# Scrape vrai.com for diamonds info

## Setup

```bash
# install virtualenv
python -m pip install --user virtualenv

# create and activate virtualenv
-d .venv || virtualenv .venv
. .venv/bin/activate

pip install -r requirements.txt
# or `poetry install` if you use poetry
```

## Notes

- There is an example response in `example_response.html` that can be use to test without hitting the server
- I did not verify if the data in the script tag is all of the contents that you would get via "infinite scrolling". Chrome WebTools didn't show any additional requests made when new "pages" of data were rendered, which implies that all of the data is delivered in the script tag.
- If the above bullet turns out to be false, first look at the other contents of the JSON and then the script tag before going back to square one to look for the data.
