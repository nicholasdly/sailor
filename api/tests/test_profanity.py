import pytest

from app import Profanity


@pytest.fixture
def profanity() -> Profanity:
    return Profanity()


def test_init(profanity: Profanity):
    assert profanity.profane_words
    assert profanity.profane_patterns
    assert len(profanity.profane_words) > 0
    assert len(profanity.profane_patterns) > 0


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
def test_censor(profanity: Profanity, text: str, expected: str):
    actual = profanity.censor(text)
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
def test_is_profane(profanity: Profanity, text: str, expected: bool):
    actual = profanity.is_profane(text)
    assert actual == expected
