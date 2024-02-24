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
    expected = "1"
    assert genome.get_source_type(0) == expected
    assert genome.from_bin_to_hex(genome.get_source_type(0), verbose=True) == int(expected)

def test_get_source_id():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "1010110"
    expected_decimal = 86
    assert genome.get_source_id(0) == expected
    assert genome.from_bin_to_hex(genome.get_source_id(0), verbose=True) == expected_decimal

def test_get_sink_type():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "1"
    expected_decimal = 1
    assert genome.get_sink_type(0) == expected
    assert genome.from_bin_to_hex(genome.get_sink_type(0), verbose=True) == expected_decimal

def test_get_sink_id():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "1110000"
    expected_decimal = 112
    assert genome.get_sink_id(0) == expected
    assert genome.from_bin_to_hex(genome.get_sink_id(0), verbose=True) == expected_decimal

def test_get_weight():
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "111000101100011"
    expected_decimal = 29027
    assert genome.get_weight(0) == expected
    assert genome.from_bin_to_hex(genome.get_weight(0), verbose=True) == expected_decimal

def test_from_hex_to_bin_back_to_hex(): # important test
    """Takes a binary input and takes it to a hexadecimal."""
    genome = Genome()
    genome.genome[0] = "6b787163"
    expected = "6b787163"
    assert genome.from_bin_to_hex((genome.from_hex_to_bin(genome.genome[0]))) == expected