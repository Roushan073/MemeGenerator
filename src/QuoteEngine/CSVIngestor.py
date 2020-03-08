
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Class for ingesting quotes from a csv file using pandas library """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest CSV file: {path}')

        quotes = []
        try:
            """ Reading the CSV File """
            df = pandas.read_csv(path, header=0)

            """ Creating a QuoteModel for each row """
            for index, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
        except Exception as e:
            raise Exception(f'Exception while reading CSV: `{path}` with Msg: {e}')

        return quotes
