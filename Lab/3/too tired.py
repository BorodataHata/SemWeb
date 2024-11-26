from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import FOAF, XSD
import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
g = Graph()

# Визначаємо простори імен
EX = Namespace("http://example.org/")  # Власний простір імен
g.bind("ex", EX)
g.bind("foaf", FOAF)

# Створення ресурсів (людей та їхніх властивостей)
cade = URIRef("http://example.org/Cade")
emma = URIRef("http://example.org/Emma")

# Додавання трійок для Кейда
g.add((cade, FOAF.name, Literal("Cade")))
g.add((cade, FOAF.based_near, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((cade, EX.degree, Literal("Bachelor of Biology", datatype=XSD.string)))
g.add((cade, EX.hasInterest, Literal("Birds, Ecology, Environment, Photography, Travel")))
g.add((cade, EX.visited, URIRef("http://example.org/Canada")))
g.add((cade, EX.visited, URIRef("http://example.org/France")))
g.add((cade, EX.graduationYear, Literal("2011", datatype=XSD.gYear)))
g.add((cade, EX.metWith, emma))
g.add((cade, EX.metPlace, Literal("Paris")))
g.add((cade, EX.metDate, Literal("2014-08-01", datatype=XSD.date)))

# Додавання трійок для Емми
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, FOAF.based_near, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, EX.degree, Literal("Master of Chemistry", datatype=XSD.string)))
g.add((emma, EX.hasInterest, Literal("Cycling, Music, Travel")))
g.add((emma, EX.visited, URIRef("http://example.org/Portugal")))
g.add((emma, EX.visited, URIRef("http://example.org/Italy")))
g.add((emma, EX.visited, URIRef("http://example.org/France")))
g.add((emma, EX.visited, URIRef("http://example.org/Germany")))
g.add((emma, EX.visited, URIRef("http://example.org/Denmark")))
g.add((emma, EX.visited, URIRef("http://example.org/Sweden")))
g.add((emma, EX.graduationYear, Literal("2015", datatype=XSD.gYear)))
g.add((emma, EX.areaOfExpertise, Literal("Waste Management, Toxic Waste, Air Pollution")))

# Збереження графу в TURTLE форматі на консоль
print(g.serialize(format="turtle"))

print("------------------------------------------------------------")

print(g.serialize(format="xml"))

with open("graph.ttl", "w", encoding="utf-8") as file:
    file.write(g.serialize(format="turtle"))

print("------------------------------------------------------------")

for triple in g:
    print(triple)

print("------------------------------------------------------------")

for triple in g:
    if "Emma" in str(triple):
        print(triple)

print("------------------------------------------------------------")

for triple in g:
    if "name" in str(triple):
        print(triple)

# Створення графа для NetworkX
G = nx.Graph()

# Додаємо вузли та зв'язки на основі RDF трійок
for s, p, o in g:
    # Використовуємо імена для зручності в графі NetworkX
    if isinstance(o, URIRef):
        G.add_edge(str(s), str(o), relation=str(p))
    elif isinstance(o, Literal):
        G.add_edge(str(s), str(o), relation=str(p))

# Візуалізація графа
plt.figure(figsize=(10, 6))  # Розмір вікна
nx.draw(G, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
plt.title("Visualized RDF Graph")
plt.show()
