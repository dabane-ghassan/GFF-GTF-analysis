#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ghassan Dabane 
GTF/GFF File analyzer.
"""


class GeneralFormat():
    def __init__(self, path):
        self.path = path

    def choose_colomn(self, colomn_num):
        """This function returns a list that contains all the specified 
        colomns from all the lines in the file.
        
        path : file path type string
        colomn_num : check README.md to know which colomn you're
        interested in isolating.
        """
        with open(self.path, 'r') as f:
            return [line.split("\t")[colomn_num - 1] for line in f]

    def tx_ID(self):
        """Returns the IDs of the transcripts in the file, and acoording to
        the supplied parameter.
        path : file path type string
        """

        return [
            attr[attr.index('transcript_id "') +
                 15:attr.index('transcript_id "') + 30]
            for attr in self.choose_colomn(colomn_num=9)
        ]  # Attributes colomn 9

    def nb_nr_tx(self):
        """This function prints out the number of non-redondant transcripts 
        in a GTF file.
        """
        print("The number of non-redondant transcripts \n in this file is %s" %
              (len(set(self.tx_ID()))))

    def ex_per_tx(self):
        """This function returns a dictionary that maps from transcript IDs to
        the number of exons present in the GTF file.
        The dictionary counter written in this function can be easily replaced
        with collections.Counter(self.tx_ID()).
        """

        e_tx = dict()
        for ID in self.tx_ID():
            if ID not in e_tx:
                e_tx[ID] = 1
            else:
                e_tx[ID] += 1
        return e_tx

    def cdna_per_tx(self):
        """This function sends back the length (in bp) of the circular dna
        for each transcript in the file, the cdna is considered as the 
        cumulated length of exons.
        """
        exon_len = [
            int(end) - int(start) + 1
            for end, start in zip(self.choose_colomn(5), self.choose_colomn(4))
        ]  # List of lengths (end colomn - start colomn) for every line in the
           # file

        cdna = dict(
        )  # Dictionray with accumulated exon length for every transcript
        for ID, LEN in zip(self.tx_ID(), exon_len):
            if ID in cdna:
                cdna[ID] += LEN
            else:
                cdna[ID] = LEN

        return cdna

    def tx_positions(self):
        """This function finds for each transcript the start position and the 
        end position in the genome, it sends back two dictionaries.
        """

        starts, ends = dict(), dict()
        for ID, start, end in zip(self.tx_ID(), self.choose_colomn(4),
                                  self.choose_colomn(5)):
            if ID not in starts:
                starts[ID] = start
                ends[ID] = end
            else:
                if start < starts[ID]:
                    starts[ID] = start
                if end > ends[ID]:
                    ends[ID] = end

        return starts, ends

    def tx_coverage(self):
        """Sends back the genomic coverage for each transcript (the
        accumulated length of introns and exons)
        """
        return {
            ID: int(end) - int(start) + 1
            for ID, start, end in zip(self.tx_positions()[0].keys(),
                                      self.tx_positions()[0].values(),
                                      self.tx_positions()[1].values())
        }      

          


