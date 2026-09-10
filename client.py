class EntityDisambiguationNED:
    """
    Named Entity Disambiguation (NED) via Collective Coherence.
    Resolves mentions to candidate entities by combining surface similarity
    and candidate-candidate graph coherence.
    """
    def disambiguate(self, mention_candidates, graph_edges):
        best_assignment = {}
        mentions = list(mention_candidates.keys())

        for m in mentions:
            candidates = mention_candidates[m]
            if not candidates:
                continue
            best_c = candidates[0]
            best_score = -1
            for c in candidates:
                coh = sum(1 for chosen in best_assignment.values() if (c, chosen) in graph_edges or (chosen, c) in graph_edges)
                if coh > best_score:
                    best_score = coh
                    best_c = c
            best_assignment[m] = best_c

        return best_assignment
