import sys
sys.path.insert(0, '../../deps/python-newick/src/')
import newick


def load_mapping(mapping_file):
    mapping = {}
    lines = open(mapping_file).readlines()
    for line in lines:
        split = line.split(" ")
        if (split[1].endswith("\n")):
            mapping[split[0]] = split[1][:-1]
        else:
            mapping[split[0]] = split[1]
    return mapping

if (len(sys.argv) != 4):
    print("Syntax: python dl_parsi_rec.py genes species map")
    sys.exit(1)

species_newick = sys.argv[1]
genes_newick = sys.argv[2]
mapping_file = sys.argv[3]

species_tree = newick.read(species_newick)
print("Species tree: " + newick.dumps(species_tree))
gene_tree = newick.read(genes_newick)
print("Gene tree: " + newick.dumps(gene_tree))
mapping = load_mapping(mapping_file)
print("Mapping: " + str(mapping))


