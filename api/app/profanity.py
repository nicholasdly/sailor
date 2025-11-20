import os
import re

from inflection import pluralize

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


class Profanity:
    profane_words: list[str] = []
    profane_patterns: list[str] = []

    def __init__(self) -> None:
        """
        Initializes an instance of `Profanity`, a profanity filter powered by regex.
        """
        self._load_profanity()

    def _load_profanity(self) -> None:
        """
        Loads the list of profane words.
        """
        words = set()

        with open(os.path.join(BASE_DIRECTORY, "data", "profanity.txt")) as f:
            for line in f:
                word = line.strip()
                if word:
                    words.add(word)
                    words.add(pluralize(word))

        # Sorts words by decreasing word length so complete profanity is
        # censored before partial profanity.
        self.profane_words = sorted(words, key=len, reverse=True)
        self.profane_patterns = [re.escape(word) for word in self.profane_words]

    def censor(self, text: str) -> str:
        """
        Returns `text` with profanity censored.
        """
        for pattern in self.profane_patterns:
            # Parse the original word, removing special characters and flags.
            word = re.sub(r"\\(.)", "\1", pattern)

            # Add word breaks to the pattern if they exist.
            if re.search(r"^\w", pattern):
                pattern = r"\b" + pattern
            if re.search(r"[^\\]\w$", pattern):
                pattern = pattern + r"\b"

            # Replaces profanity with asterisks of equal length.
            text = re.sub(r"(?i)" + pattern, "*" * len(word), text)

        return text

    def is_profane(self, text: str) -> bool:
        """
        Returns a boolean representing whether or not `text` contains profanity.
        """
        return self.censor(text) != text
