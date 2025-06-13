"""Example unit tests."""

from PyTemplate import __version__


def test_version_type():
    """Test defined version is a string."""
    assert isinstance(__version__, str), "Expected string format version"


def test_version_value():
    """Test version string starts with the letter v."""
    assert __version__.lower().startswith("v"), "Expected version to begin with `v`"
