from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """ Generic class for ingesting quotes form various file types """
    ingestors = [CSVIngestor, DocxIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        try:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            raise Exception(f'No parser found for File: `{path}`')
        except Exception as e:
            raise Exception(f'Exception while reading File: `{path}` with Msg: {e}')
