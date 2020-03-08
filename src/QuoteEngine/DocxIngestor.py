
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """ Class for ingesting quotes from a docx file using python-docx library """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest Docx file: {path}')

        quotes = []
        try:
            """ Reading the Docx File """
            doc = docx.Document(path)

            """ Creating a QuoteModel for each row """
            for para in doc.paragraphs:
                if para.text != "":
                    """ Body and Author are separated by ' - ' """
                    parse = para.text.split(' - ')
                    new_quote = QuoteModel(parse[0].replace('"', ''), parse[1])
                    quotes.append(new_quote)
        except Exception as e:
            raise Exception(f'Exception while reading: DOCX`{path}` with Msg: {e}')

        return quotes
