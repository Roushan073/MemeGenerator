from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ Class for ingesting quotes from a pdf file using pdftotext and subprocess """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest PDF file: {path}')

        tmp = f'./tmp/pdf_to_text_{random.randint(0, 100000000)}.txt'

        """ Reading content of PDF file and writing to a text file """
        call = subprocess.call(['pdftotext', path, tmp])

        """ Using TXTIngestor class to parse the tmp `txt` file and get the Quotes """
        quotes = TXTIngestor.parse(tmp)
        os.remove(tmp)

        return quotes
