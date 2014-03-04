import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

L = 5 # number of rows in matrix A
M = 5 # number of columns and rows in matrices A and B, respectively
N = 5 # number of columns in matrix B

def mapper(record):
    matrix = record[0]
    row = record[1]
    column = record[2]
    value = record[3]
    if matrix == 'a':
        for k in range(N): mr.emit_intermediate((row,k), {column:value})
    if matrix == 'b':
        for i in range(L): mr.emit_intermediate((i,column), {row:value})

def reducer(key, list_of_values):
    #total = sum(i*j for i, j in zip(list_of_values[:M], list_of_values[M:]))
    dot = [[x[k] for x in list_of_values if k in x.keys()] for k in range(M)]
    total = sum((x[0]*x[1] for x in dot if len(x) == 2))
    mr.emit(key + (total,))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
