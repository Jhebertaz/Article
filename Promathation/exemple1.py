domaine = range(-3,4)
f = lambda x: x**2
graph = [(x,f(x)) for x in domaine]

def preimageSearch(graph, image):
	preimage = []
	for point in graph:
		if point[1] == image:
			preimage.append(point[0])
	return preimage

print(preimageSearch(graph, 4))
