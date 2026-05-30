from rdflib import Graph, URIRef

g = Graph()

goa = URIRef("http://example.org/Goa")
beach = URIRef("http://example.org/Beach")

g.add(
    (
        goa,
        URIRef("http://example.org/hasActivity"),
        beach
    )
)

print("Triples in Graph:")

for s, p, o in g:
    print(s, p, o)

g.serialize("graph.ttl")
