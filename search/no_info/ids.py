from search.no_info.dls import depthLimitedSearch

def iterativeDepthSearch(problem):
    depth = 0
    while True:
        resultado = depthLimitedSearch(problem, depth, True)
        if resultado != 'cutoff':
            return resultado
        depth+=1
