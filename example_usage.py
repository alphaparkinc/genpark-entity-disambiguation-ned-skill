from client import EntityDisambiguationNED

def main():
    print("=== Testing Named Entity Disambiguation (NED) ===")
    ned = EntityDisambiguationNED()

    candidates = {
        "Apple": ["Apple_Inc", "Apple_Fruit"],
        "Jobs": ["Steve_Jobs", "Employment_Listing"]
    }
    graph_edges = {("Apple_Inc", "Steve_Jobs")}

    results = ned.disambiguate(candidates, graph_edges)
    print("Disambiguation results:", results)
    assert results["Apple"] == "Apple_Inc"
    assert results["Jobs"] == "Steve_Jobs"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
