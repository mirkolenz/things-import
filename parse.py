import ruamel.yaml
import json
import sys
import urllib.parse
import os

things_prefix = "things:///json?data="
templates_folder = "templates/"

yaml_parser = ruamel.yaml.YAML(typ="safe")
results = {}

filenames = [file for file in os.listdir(sys.argv[1]) if file.endswith(".yml")]
for filename in filenames:
    with open(os.path.join(templates_folder, filename)) as file:
        yaml_data = yaml_parser.load(file)
        json_data = json.dumps(yaml_data, ensure_ascii=False)
        things_str = things_prefix + urllib.parse.quote(json_data)

        key = filename.replace(".yml", "").replace("-", " ")
        results[key] = things_str.strip()

list_str = ""
for key, value in sorted(results.items()):
    list_str += f"<li><a href='{value}'>{key}</a></li>"

with open(sys.argv[2], "w") as file:
    file.writelines(
        """
        <html>
            <head>
                <title>Things 3 Templates</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.css'>
            </head>
            <body>
                <h1>Things 3 Templates</h1>
                <ul>"""
        + list_str
        + """
                </ul>
            </body>
        </html>
    """
    )
