def minimum_cardinality_set_of_intervals(L, R):
    n = len(L)
    intervals = [(L[i], R[i]) for i in range(n)]
    intervals.sort(key=lambda x: x[1]) # ordena por sus puntos finales de menor a mayor
    result_set = set()
    last_point = -float('inf')
    # print(intervals)
    for interval in intervals:
        if interval[0] > last_point:
            result_set.add(interval[1])
            last_point = interval[1]
    return result_set

A = [4,5,0,11,1,10,5]
B = [7,10,3,14,5,13,9]

Res = [2,6,11]

print (minimum_cardinality_set_of_intervals(A,B))
