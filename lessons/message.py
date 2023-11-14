"""Class to store a message (operator overload, union types, default parameters)!"""


class Email:

    to: str
    message: str
    important: bool

    def __init__(self, recipient: str, message_text: str, importance_flag: bool):
        """Constructor of an email!"""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag
    
    def __str__(self) -> str:
        """Docstring!"""
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int):
        """Lil Docstring!"""
        self.message *= factor


email_to_chiara: Email = Email("David", "You're so sexy! ", False)
email_to_chiara * 100
print(email_to_chiara)