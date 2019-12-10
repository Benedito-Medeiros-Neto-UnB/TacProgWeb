from owlready2 import *

onto_path.append(".")
onto_teses = get_ontology("http://127.0.0.1/onto_teses.owl")

with onto_teses:
    class Teses