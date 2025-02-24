import pytest
from mecab_ko_.mecab import MeCab


@pytest.fixture
def mecab():
    return MeCab()
