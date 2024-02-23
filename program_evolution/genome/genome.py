"""Genome class and utility functions."""
import secrets


class Genome:

    def __init__(self, genome_size, genome:list=[], num_bytes_gene=4):
        self.genome = genome
        self.genome_size = genome_size
        self.num_bytes_gene = num_bytes_gene

    def create_brain(self):
        """Takes genes iteratively and creates connections between blank/initial neuron map."""

    def random_genome(self) -> list:
        for _ in range(self.genome_size):
            self.genome.append(secrets.token_hex(self.num_bytes_gene))  # 4 bytes = 8 hex characters

    def get_source_type(self) -> int:
        """Returns first bit """

    def from_hex_to_bin(self, hex, verbose=False) -> str:
        """Takes hex numerical input (not string) and returns binary string."""
        hex = int(hex, 16)
        if verbose:
            return int(bin(hex)[2:], 2)
        # print(int(attemp.from_bin_to_hex(0b1111), 16)) <- to get to int type 
        return bin(hex)[2:]
    
    def from_bin_to_hex(self, bin, verbose=False) -> str: 
        """Takes numerical binary input (not string) and returns hex string."""
        bin = int(bin, 2)
        if verbose:
            return int(hex(bin)[2:], 16)
        # print(int(attemp.from_hex_to_bin(0x1f), 2)) <- to get to int type 
        return hex(bin)[2:]