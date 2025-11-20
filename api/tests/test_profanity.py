import pytest

from app import Sailor


@pytest.fixture
def sailor() -> Sailor:
    return Sailor()


def test_init(sailor: Sailor):
    assert sailor.profane_words
    assert sailor.profane_patterns
    assert len(sailor.profane_words) > 0
    assert len(sailor.profane_patterns) > 0


@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world", "hello world"),
        ("legendary fox", "legendary fox"),
        ("bash it", "bash it"),
        ("kevin cockenson", "kevin cockenson"),
        ("damn the world", "**** the world"),
        ("what the fuck", "what the ****"),
        ("take a piss", "take a ****"),
        ("who gives a shi+", "who gives a ****"),
        ("bi7ch d4mn", "***** ****"),
    ],
)
def test_censor(sailor: Sailor, text: str, expected: str):
    actual = sailor.censor(text)
    assert actual == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("hello world", False),
        ("legendary fox", False),
        ("bash it", False),
        ("kevin cockenson", False),
        ("damn the world", True),
        ("what the fuck", True),
        ("take a piss", True),
        ("who gives a shi+", True),
        ("bi7ch d4mn", True),
    ],
)
def test_is_profane(sailor: Sailor, text: str, expected: bool):
    actual = sailor.is_profane(text)
    assert actual == expected
