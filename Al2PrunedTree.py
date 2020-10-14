import argparse
import ete3
from Bio import SeqIO
import os

usage = "A script to prune a given newick tree keeping only taxa present in a given sequence alignment (FASTA format)"
toolname = "Al2PrunedTree"
footer = "Who \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n November 2019; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)

parser.add_argument('-t', metavar = 'filename', dest = 'tree', required = True,
                    help = 'path to the input newick tree file')
parser.add_argument('-a', metavar = 'filename', dest = 'alignment', required = True,
                    help = 'path to the input multiple sequence alignment file')

args = parser.parse_args()
input_tree = args.tree
input_alignment = args.alignment

tree = ete3.Tree(input_tree)
alignment = SeqIO.parse(input_alignment, "fasta")

tree_leaves = tree.get_leaf_names()
alignment_taxa = []

for record in alignment:
    alignment_taxa.append(record.id)

to_remove = []

for taxon in tree_leaves:
    if taxon not in alignment_taxa:
        to_remove.append(taxon)

if len(to_remove) > 0:        
    to_remove_for_newick_tools = ""
    
    for taxon in to_remove:
        to_remove_for_newick_tools += taxon 
        to_remove_for_newick_tools += ","
    
    to_remove_for_newick_tools = to_remove_for_newick_tools[:-1]
    
    newick_tools_command = "newick-tools --prune_tips " + to_remove_for_newick_tools + " --tree_file " + input_tree + " --output " + input_alignment + "." + input_tree.split(".")[0] + ".pruned.nwk"
    
    
    os.system(newick_tools_command)
elif len(to_remove) == 0:
    print("No taxa to remove")
    os.system("cp " + input_tree + " " + input_alignment + "." + input_tree.split(".")[0] + ".pruned.nwk")

print("----------------------------------------------------------------------------------------------------------------")