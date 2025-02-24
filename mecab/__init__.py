from .mecab import MeCab, MeCabError, mecabrc_path
from .types import Dictionary, Feature, Morpheme, Span

print(111, MeCab)

__version__ = "1.3.7"

__all__ = [
    "MeCab",
    "Morpheme",
    "Span",
    "Feature",
    "Dictionary",
    "MeCabError",
    "mecabrc_path",
]
