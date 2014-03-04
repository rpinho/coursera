import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record
    key.sort()
    mr.emit_intermediate(tuple(key), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = sum(list_of_values)
    if total < 2:
        mr.emit(key)
        mr.emit(key[::-1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
