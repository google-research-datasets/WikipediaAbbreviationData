"""Utility methods for textproto IO."""

import logging

from typing import TextIO

from google.protobuf import text_format  # type: ignore

import abbreviation_pb2


def read_corpus(source: TextIO) -> abbreviation_pb2.AbbreviationCorpus:
    """Reads corpus textproto from file handle."""
    corpus = abbreviation_pb2.AbbreviationCorpus()
    text_format.ParseLines(source, corpus)
    logging.debug("Read %d sentences", len(corpus.sentences))
    return corpus
