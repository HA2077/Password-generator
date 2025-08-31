import string
import pytest
import password_generator

def test_password_length():
    pw = password_generator.Passgen(
        Length=16,
        UseLowercase=True,
        UseUppercase=True,
        UseSymbol=True,
        UseNumber=True,
        Lowercase=string.ascii_lowercase,
        Uppercase=string.ascii_uppercase,
        Symbol="!@#$%^&*()_+-=[]{}|;:,.<>?/~",
        Number=string.digits
    )
    assert len(pw) == 16

def test_password_contains_lowercase():
    pw = password_generator.Passgen(
        Length=32,
        UseLowercase=True,
        UseUppercase=False,
        UseSymbol=False,
        UseNumber=False,
        Lowercase=string.ascii_lowercase,
        Uppercase=string.ascii_uppercase,
        Symbol="!@#$%^&*()_+-=[]{}|;:,.<>?/~",
        Number=string.digits
    )
    assert any(c in string.ascii_lowercase for c in pw)

def test_password_contains_uppercase():
    pw = password_generator.Passgen(
        Length=12,
        UseLowercase=False,
        UseUppercase=True,
        UseSymbol=False,
        UseNumber=False,
        Lowercase=string.ascii_lowercase,
        Uppercase=string.ascii_uppercase,
        Symbol="!@#$%^&*()_+-=[]{}|;:,.<>?/~",
        Number=string.digits
    )
    assert any(c in string.ascii_uppercase for c in pw)

def test_password_contains_number():
    pw = password_generator.Passgen(
        Length=10,
        UseLowercase=False,
        UseUppercase=False,
        UseSymbol=False,
        UseNumber=True,
        Lowercase=string.ascii_lowercase,
        Uppercase=string.ascii_uppercase,
        Symbol="!@#$%^&*()_+-=[]{}|;:,.<>?/~",
        Number=string.digits
    )
    assert any(c in string.digits for c in pw)

def test_password_contains_symbol():
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    pw = password_generator.Passgen(
        Length=11,
        UseLowercase=False,
        UseUppercase=False,
        UseSymbol=True,
        UseNumber=False,
        Lowercase=string.ascii_lowercase,
        Uppercase=string.ascii_uppercase,
        Symbol=symbols,
        Number=string.digits
    )
    assert any(c in symbols for c in pw)

def test_no_character_type_selected():
    with pytest.raises(IndexError):
        password_generator.Passgen(
            Length=8,
            UseLowercase=False,
            UseUppercase=False,
            UseSymbol=False,
            UseNumber=False,
            Lowercase=string.ascii_lowercase,
            Uppercase=string.ascii_uppercase,
            Symbol="!@#$%^&*()_+-=[]{}|;:,.<>?/~",
            Number=string.digits
        )
