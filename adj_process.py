from mrjob.protocol import JSONProtocol
from collections import defaultdict
import sys

if __name__ == "__main__":
  jason = JSONProtocol()
  input_file = sys.argv[-1]
  with open(input_file, 'r') as f:
    data = [x.split() for x in f.read().splitlines()]

  nodes = defaultdict(list)
  for link in data:
    if len(link) == 1: # dangling nodes
      nodes[link[0]] = []
    else:
      nodes[link[0]].append(link[1:][0])

  with open("adj_" + input_file, "wb+") as f:
    for id, adj in nodes.items():
      n_nodes = len(nodes)
      if len(adj) == 0:
        f.write(jason.write(id, (adj, 0.0))) # initial prob of dangling nodes: 0
      else:
        f.write(jason.write(id, (adj, 1/n_nodes))) # initial prob: 1/n
      f.write('\n'.encode('utf-8')) 