"""Genome class and utility functions."""


class Genome:

    def __init__(self,):
        pass

    def create_brain(self):
        """Takes genes iteratively and creates connections between blank/initial neuron map."""

    def from_hex_to_bin(self, hex) -> str:
        """Takes hex numerical input (not string) and returns binary string."""
        # print(int(attemp.from_bin_to_hex(0b1111), 16)) <- to get to int type 
        return bin(hex)[2:]
    
    def from_bin_to_hex(self, bin) -> str: 
        """Takes numerical binary input (not string) and returns hex string."""
        # print(int(attemp.from_hex_to_bin(0x1f), 2)) <- to get to int type 
        return hex(bin)[2:]