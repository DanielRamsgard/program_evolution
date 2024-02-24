"""Genome class and utility functions."""
import secrets
import random


class Genome:

    def __init__(self, genome_size=8, genome:list=[], num_bytes_gene=4): # size is number of geners; genome list is actual genes
        self.set_genome_size(genome_size)
        self.set_num_bytes_gene(num_bytes_gene)
        self.set_genome(genome)

    def get_genome_size(self):
        return self.genome_size

    def get_num_bytes_gene(self):
        return self.num_bytes_gene

    def get_genome(self):
        return self.genome

    def set_genome(self, genome:list):
        """Sets the genome."""
        self.genome = genome
        if len(genome) != 0:
            return
        for _ in range(self.genome_size):
            self.genome.append(secrets.token_hex(self.num_bytes_gene))  # 4 bytes = 8 hex characters

    def set_genome_size(self, genome_size):
        """Sets the size of genome."""
        self.genome_size = genome_size
    
    def set_num_bytes_gene(self, num):
        self.num_bytes_gene = num

    def create_brain(self):
        """Takes genes iteratively and creates connections between blank/initial neuron map."""

    def get_weight(self, i):
        while (i > len(self.genome) - 1):
            i = input("Your index is too large. Reenter an index: ")
        return self.from_hex_to_bin(self.genome[i])[16:32]
    
    def mutation(self):
        """get the binary string and change a random index to the opposite value."""
        i = random.randint(0,self.genome_size-1)
        current_gene = self.from_hex_to_bin(self.genome[i])
        j = random.randint(0,self.num_bytes_gene*8-1)
        mutation = current_gene[j]
        if mutation == "1":
            mutation = "0"
        else: 
            mutation = "1"
        self.genome[i][j] = mutation

    def get_sink_id(self, i):
        """get_sink_id"""
        while (i > len(self.genome) - 1):
            i = input("Your index is too large. Reenter an index: ")
        return self.from_hex_to_bin(self.genome[i])[9:16]

    def get_sink_type(self, i):
        """get_sink_type"""
        while (i > len(self.genome) - 1):
            i = input("Your index is too large. Reenter an index: ")
        return self.from_hex_to_bin(self.genome[i])[8]

    def get_source_id(self, i):
        """get_source_id"""
        while (i > len(self.genome) - 1):
            i = input("Your index is too large. Reenter an index: ")
        return self.from_hex_to_bin(self.genome[i])[1:8]

    def get_source_type(self, i) -> int:
        """Returns first bit of any given gene given an input index."""
        while (i > len(self.genome) - 1):
            i = input("Your index is too large. Reenter an index: ")
        return self.from_hex_to_bin(self.genome[i])[0]


    def from_hex_to_bin(self, hex, verbose=False):
        """Takes hex numerical input (not string) and returns binary string; if True verbose, then numerical integer is returned."""
        hex = int(hex, 16)
        if verbose:
            return int(bin(hex)[2:], 2)
        # print(int(attemp.from_bin_to_hex(0b1111), 16)) <- to get to int type 
        return bin(hex)[2:]
    
    def from_bin_to_hex(self, bin, verbose=False): 
        """Takes numerical binary input (not string) and returns hex string; if True verbose, then numerical integer is returned."""
        bin = int(bin, 2)
        if verbose:
            return int(hex(bin)[2:], 16)
        # print(int(attemp.from_hex_to_bin(0x1f), 2)) <- to get to int type 
        return hex(bin)[2:]