class IsStringLong:
    def __init__(self) -> None:
        self.last_string_long = False

    def is_long(self, text: str) -> bool:
        result = True if len(text) > 5 else False
        if result:
            self.last_string_long = True
        # self.last_string_long = result

        return result
