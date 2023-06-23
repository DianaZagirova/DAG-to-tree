import pickle
import networkx as nx
from DAG_to_tree import dag2tree

with open('EFO_graph.pkl', 'rb') as f:
    dag = pickle.load(f)

root_node = 'EFO_0000408'
tree = dag2tree(dag, root_node)