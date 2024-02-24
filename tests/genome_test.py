"""Tests for the genome.py file."""
from ..program_evolution.genome import Genome

def test_bin_to_hex() -> None:
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "1101011011110000111000101100011"
    expected = "6b787163"
    assert genome.from_bin_to_hex(genome.genome[0]) == expected


def test_bin_to_hex_to_decimal():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "1101011011110000111000101100011"
    expected = 1803055459
    assert genome.from_bin_to_hex(genome.genome[0], verbose=True) == expected

def test_hex_to_bin() -> None:
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "1101011011110000111000101100011"
    assert genome.from_hex_to_bin(genome.genome[0]) == expected


def test_hex_to_bin_to_decimal():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = 1803055459
    assert genome.from_hex_to_bin(genome.genome[0], verbose=True) == expected

def test_get_source_type():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = 1
    assert genome.get_source_type(0) == expected