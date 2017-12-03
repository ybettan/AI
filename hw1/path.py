class Path:
    roads = None
    junctions = None
    links = None

    def __init__(self, roads, junctions):
        assert len(junctions) > 0, "A path must contain at least one junction"

        self.roads = roads
        self.junctions = [self.roads[j] for j in junctions]
        self.links = []

        # Get links
        for s,t in zip(junctions[:-1], junctions[1:]):
            wasFound = False
            for l in self.roads[s].links:
                if l.target == t:
                    self.links.append(l)
                    wasFound = True
                    break

            assert wasFound, "Two adjacent vertices in the path have no link between them"

    # Returns path length in meters
    def getDistance(self):
        return sum([l.distance for l in self.links])
