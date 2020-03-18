from collections import defaultdict


def to_adj_list(gjson, directed=True, alpha=False):
    g = defaultdict(list)
    w = defaultdict(int)
    for edges in gjson["el"].values():
        if alpha:
            g[chr(edges['u'] + 97)].append(chr(edges['v'] + 97))
            w[chr(edges['u'] + 97), chr(edges['v'] + 97)] = int(edges['w'])
        else:
            g[edges['u']].append(edges['v'])
            w[edges['u'], edges['v']] = int(edges['w'])
    if directed:
        print('graph adjacent list')
        print(dict(g))
        print('weights')
        print(dict(w))
        return
    # make undirected
    dg = defaultdict(list)
    for k, v in g.items():
        for e in v:
            dg[k].append(e)
            dg[e].append(k)
    print('graph adjacent list')
    print(dict(dg))
    uw = defaultdict(list)
    for k, v in w.items():
        uw[k] = v
        uw[(k[1], k[0])] = v
    print('weights')
    print(dict(uw))


# graph json format is from https://visualgo.net
gjson = {"vl": {"0": {"x": 60, "y": 40}, "1": {"x": 60, "y": 120}, "2": {"x": 180, "y": 80}, "3": {"x": 300, "y": 140},
                "4": {"x": 120, "y": 240}, "5": {"x": 300, "y": 260}, "6": {"x": 380, "y": 40},
                "7": {"x": 420, "y": 220}, "8": {"x": 460, "y": 100}},
         "el": {"0": {"u": 0, "v": 1, "w": "8"}, "1": {"u": 0, "v": 2, "w": "12"}, "2": {"u": 1, "v": 2, "w": "13"},
                "3": {"u": 1, "v": 4, "w": "9"}, "4": {"u": 2, "v": 3, "w": "14"}, "5": {"u": 1, "v": 3, "w": "25"},
                "6": {"v": 3, "u": 4, "w": "20"}, "7": {"u": 2, "v": 6, "w": "21"}, "8": {"u": 3, "v": 6, "w": "12"},
                "9": {"u": 6, "v": 8, "w": "11"}, "10": {"u": 3, "v": 8, "w": "16"}, "11": {"u": 3, "v": 7, "w": "12"},
                "12": {"u": 7, "v": 8, "w": "9"}, "13": {"u": 4, "v": 5, "w": "19"}, "14": {"u": 5, "v": 7, "w": "11"},
                "15": {"u": 3, "v": 5, "w": "8"}}}

to_adj_list(gjson, directed=False, alpha=False)
