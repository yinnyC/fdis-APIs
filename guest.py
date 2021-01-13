"""Define class Guest."""


class Guest:
    """Class guest holds important guest properties."""

    def __init__(self, name, email, plus_one, phone):
        """Initialize guest properties."""
        self.name = name
        self.email = email
        self.plus_one = plus_one
        self.phone = phone
