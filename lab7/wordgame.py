import networkx as nx


def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph(filename,n):
    f = open(filename,'r')
    words = set()
    for line in f.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:n])
        words.add(w)
    return generate_graph(words)

if __name__ == '__main__':
    G = words_graph('words.dat',5) # Graph of 5 letter words
    print "Loaded words_dat.txt containing five-letter English words"
    print "Two words are connected if they differ in one letter"
    print "Graph has %d nodes with %d edges"%(nx.number_of_nodes(G), nx.number_of_edges(G))
    print "%d connected components"%(nx.number_connected_components(G))

    for(source, target) in [('chaos','order'),
                            ('nodes','graph'),
                            ('moron','smart'),
                            ('pound','marks')]:
        print "Shortest path between %s and %s is"%(source, target)
        try:
            sp = nx.shortest_path(G, source, target)
            for word in sp:
                print word
        except nx.NetworkXNoPath:
            print "No Path"

    G = words_graph('words4.dat',4) # Graph of 4 letter words
    print "Loaded words_dat.txt containing four-letter English words"
    print "Two words are connected if they differ in one letter"
    print "Graph has %d nodes with %d edges"%(nx.number_of_nodes(G), nx.number_of_edges(G))
    print "%d connected components"%(nx.number_connected_components(G))

    for(source, target) in [('cold','warm'),
                            ('love','hate')]:
        print "Shortest path between %s and %s is"%(source, target)
        try:
            sp = nx.shortest_path(G, source, target)
            for word in sp:
                print word
        except nx.NetworkXNoPath:
            print "No Path"
        
