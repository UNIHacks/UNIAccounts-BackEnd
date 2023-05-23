import json
import os
import sys


def generate_markdown(config: dict, this_dir: str, version_api: str):
    data = ""
    try:
        for file in config["files"]:
            with open(f"{this_dir}/docs/{version_api}/{file}") as file:
                data += file.read() + "\n"
        with open(f"{this_dir}/docs/api_{version_api}.md", "w") as file:
            file.write(data)
        print("Successful Generate API Docs")
    except ValueError as e:
        print(e)
        print("Error Generate API Docs")


# TODO: Create This Funtion
def generate_pdf(config: dict, this_dir: str, version_api: str):
    generate_markdown(config=config, this_dir=this_dir, version_api=version_api)


output_types = {
    "md": generate_markdown,
    "pdf": generate_pdf,
}


def main():
    try:
        version_api = sys.argv[1]
        output_type = sys.argv[2]

        this_dir = os.getcwd()

        file_config = open(f"{this_dir}/docs/{version_api}/config.json", "r")
        config = json.load(file_config)

        output_types[f"{output_type}"](
            config=config, this_dir=this_dir, version_api=version_api
        )

    except SystemError as e:
        print(e)
        print("Error Generate API Docs")


if __name__ == "__main__":
    main()
