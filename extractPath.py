def extractPath(parent,src,dest):
    curr = dest
    path = []
    while parent[curr] is not None:
        path.append(curr)
        print(curr)
        curr = parent[curr]

    path.append(curr)
    return path