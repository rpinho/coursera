import MapReduce
import sys, itertools

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    orders = (v for v in list_of_values if v[0] == 'order')
    line_items = (v for v in list_of_values if v[0] == 'line_item')
    for order, line_item in itertools.product(orders, line_items):
        mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
