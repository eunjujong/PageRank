from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONProtocol

class Pagerank(MRJob):
  INPUT_PROTOCOL = JSONProtocol
  n_nodes = 0
  def configure_args(self):
    super(Pagerank, self).configure_args()

    self.add_passthru_arg('--iterations', default=50, type=int) # iteration to achieve pagerank convergence
    self.add_passthru_arg('--a', default=0.85, type=float) # random jump factor a = (1-m)

  def mapper(self, nid, node):
    global n_nodes
    adj_list, pagerank = node
    n_nodes = len(adj_list)
    if n_nodes == 0:    # pagerank of 0 for dangling nodes
      p = 0
    else:
      p = pagerank / n_nodes  
    yield nid, ('node', node)   # pass graph structure

    for adj_id in adj_list:
      yield adj_id, ('PR_mass', p)    # pass pageRank mass to neighbors

  def reducer(self, nid, values):
    M = {}
    total_score = 0
    for label, val in values:
      if label == 'node':
        M = val                     # recover graph structure
      elif label == 'PR_mass':
        total_score += float(val)   # sum incoming PageRank contributions

    a = self.options.a
    if n_nodes == 0:
      M[1] = total_score
    else: 
      M[1] = total_score*a + (1-a)/n_nodes  # pagerank with random jump factor (->dangling nodes)
    yield nid, M

  def steps(self):
    iter = self.options.iterations
    return [
      MRStep(mapper=self.mapper,
      reducer=self.reducer)
    ] * iter

if __name__ == "__main__":
  Pagerank.run()