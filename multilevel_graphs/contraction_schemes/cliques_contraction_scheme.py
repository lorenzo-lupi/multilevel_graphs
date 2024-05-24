from multilevel_graphs.contraction_schemes import ContractionScheme
from multilevel_graphs.dec_graphs import DecGraph, enumerate_all_cliques
from multilevel_graphs.contraction_schemes import DecTable


class CliquesContractionScheme(ContractionScheme):
    def __init__(self, level: int, reciprocal: bool = False):
        super().__init__(level)
        self._reciprocal = reciprocal

    @property
    def contraction_name(self) -> str:
        return "cliques_" + ("" if self._reciprocal else "not_") + "rec"

    def contraction_function(self, dec_graph: DecGraph) -> DecTable:
        cliques = enumerate_all_cliques(dec_graph, self._reciprocal)
        return DecTable(cliques)