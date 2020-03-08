
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """ Class for ingesting quotes from a txt file """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest TXT file: {path}')

        quotes = []
        try:
            """ Reading the Docx File """
            file_ref = open(path, "r", encoding='utf-8')

            """ Creating a QuoteModel for each row """
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    """ Body and Author are separated by ' - ' """
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0].replace('"', ''), parse[1])
                    quotes.append(new_quote)
            file_ref.close()

        except Exception as e:
            raise Exception(f'Exception while reading TXT: `{path}` with Msg: {e}')

        return quotes
