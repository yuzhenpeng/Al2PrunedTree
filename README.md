# Al2PrunedTree
Prunes a given newick tree file to keep only taxa present in a given sequence alignment (FASTA format)


## Dependencies
- [Python 3.x](https://www.python.org)
- [Biopython](https://biopython.org)
- [ETE toolkit](http://etetoolkit.org)
- [newick-tools](https://github.com/xflouris/newick-tools)

## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-t filename | tree file (newick format)
-a dirname | alignment file (FASTA format)
<br>   

## Example usage

```
python3 Al2PrunedTree.py -t tree_file.nwk -a alignment_file.fasta
```
<br>

======================================================================================

<br>

Who<br> 
 Paschalis Natsidis (p.natsidis@ucl.ac.uk); <br>
<br>
Where<br>
 Telford Lab, UCL; <br>
 ITN IGNITE; 
<br>
<br>
When<br> 
 October 2020; 
