# Meme Generator

Meme Generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote using command-line interface (CLI) or web-app. The project will be interacting with variety of file types (csv, docx, pdf, txt) to load quotes from.

# Install

If you have multiple versions of Python installed on your machine, please be mindful [to set up a virtual environment with Python 3](https://docs.python.org/3/library/venv.html).

## To Setup a Python 3  Virtual  Environment

```python3 -m venv /path/to/new/virtual/environment```

## To install the dependencies

```pip3 install -r /path/to/requirements.txt```

# Usage

To use the project:

1. Clone the project to your local machine
2. Create a virtual environment, named `venv`, with `python3 -m venv /venv` in project root
3. Activate the virtual environment with `source venv/bin/activate`
4. Navigate to the `/src` directory
5. Run `python3 meme.py -h` for an explanation of how to run the project (CLI) or Run `python3 app.py` to launch a web-app and interact with the application.
6. Or try it out yourself!

Example of how to use the interface:

1. Generate A Meme

`python3 ./meme.py --path ./_data/photos/dog/xander_1.jpg --body Sample Quote --author Author`

## Project Organization

The project is broken into the following files:

- `meme.py`: Python script to generate a meme using command-line interface (CLI). 
- `app.py`: Python script to generate meme using web-app.
- `MemeEngine`: Python package containing modules for generate a meme (an image with an overlaid quote)
- `QuoteEngine`: Python package containing modules to ingest quotes (Body and Author) from a variety of filetypes (PDF, Word Documents, CSVs, Text files)
- `data` - directory containing sample imgaes and quotes

