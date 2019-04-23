# Things URL Import

## Requirements

- Python 3
- pipenv
- Optional: make

## Installation

`pipenv install`

## Usage

First, create a folder `templates`. Inside that folder, you can create as many templates as you like as `.yml` files. You have to follow the [official Things 3 URL scheme](https://support.culturedcode.com/customer/en/portal/articles/2803573), but as we are using YML, the syntax is much cleaner. Here is an example:

```yaml
---
- type: project
  attributes:
    title: Title of the Project
    area: Area that it should be appended to
    items:
      - type: heading
        attributes:
          title: Subtitle
      - type: to-do
        attributes:
          title: Actual Todo item
```

You are not limited to project imports, it is possible to represent every option supported by Things.

To actually transcode the templates into a web page with usable links, run the following command: `pipenv run python parse.py FILENAME`

The resulting file can be uploaded to your webserver for easy import.

## Automation

```makefile
CC = pipenv run python
OUTFILE = "things3.html"
SSH = "username@server"

.PHONY: all

all: $(OUTFILE) upload

$(OUTFILE): parse.py templates/*
	$(CC) $< $(OUTFILE)

upload: $(OUTFILE)
	scp -rp $(OUTFILE) $(SSH)
```
