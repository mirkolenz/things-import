# Things URL Import

## Requirements

- Python 3
- poetry
- make

## Installation

1. `make install`.
2. Create a folder named `templates`.

## Usage

Inside `templates`,  you can create as many templates as you like as `.yml` files.
You have to follow the [official Things 3 URL scheme](https://support.culturedcode.com/customer/en/portal/articles/2803573), but as we are using YML, the syntax is much cleaner.
Here is an example:

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

To run the program, simply call `make`.
The resulting file can be uploaded to your webserver for easy import.
