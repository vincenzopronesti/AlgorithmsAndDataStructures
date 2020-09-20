# AlgorithmsAndDataStructures

- `binomialHeapRelax` contains a Python implementation of the binomial heap data structure. 
	With regular binomial heaps, every time the data structure is modified, a merging process is issued because only one $B_i$ tree is allowed in the forest.
	This particular implementation allowa to have more than one $B_i$ tree. In fact, the merging process is executed only when a `deleteMin` operation is requested.