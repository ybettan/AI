'accessible using "import ways.draw"'

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError('Please install matplotlib:  http://matplotlib.org/users/installing.html#windows')

plt.axis('equal')

def plotOrders(roads, orders):
    from matplotlib import pyplot as plt
    for i,order in enumerate(orders):
        ps, pt = roads[order[0]], roads[order[1]]

        # Draw source
        plt.scatter([ps.lon], [ps.lat], c='r', marker='o')
        plt.annotate("s{}".format(i + 1), [ps.lon + 0.001, ps.lat])

        # Draw target
        plt.scatter([pt.lon], [pt.lat], c='b', marker='x', s=80)
        plt.annotate("t{}".format(i + 1), [pt.lon + 0.001, pt.lat])

def plotPath(path, color=None, marker=None):
    '''path is a list of junction-ids - keys in the dictionary.
    e.g. [0, 33, 54, 60]
    Don't forget plt.show()'''
    flons, tolons, flats, tolats = [], [], [], []
    #for l in path.links:
    for ps,pt in zip(path.junctions[:-1], path.junctions[1:]):
        flons.append(ps.lon)
        tolons.append(pt.lon)
        flats.append(ps.lat)
        tolats.append(pt.lat)

    plt.plot(flons, flats, tolons, tolats, color=color, marker=marker)


