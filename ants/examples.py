
from support import read_sample
from ants.clustering import clustering

def templateClustering( file, num_ants, size_lattice, count_iteration ):
    sample = read_sample(file);
    return clustering( num_ants, size_lattice, count_iteration, sample, len(sample) )


def ClusteringSampleSimple1():
    print( templateClustering( '../samples/SampleSimpleForAntsClustering1.txt', 10, 11, 10000 ) )


ClusteringSampleSimple1()