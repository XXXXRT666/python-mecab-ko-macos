import pytest

from mecab_ko.mecab import MeCab


@pytest.fixture
def mecab():
    return MeCab()
