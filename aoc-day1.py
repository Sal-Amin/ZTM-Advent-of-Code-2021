def depth_measure(li):
  """Takes a list of measures compares with the previous measure and yields if the depth increased or decreased"""
  pre_dep = 0
  dep_measure = []
  for i in range(len(li)):
    if i == 0:
      pre_dep = li[i]
      dep_measure.append("N/A - no previous measurement")
    elif i > 0 and li[i] > pre_dep:
      pre_dep = li[i]
      dep_measure.append("increased")
    elif i > 0 and li[i] < pre_dep:
      pre_dep = li[i]
      dep_measure.append("decreased")
    elif i > 0 and li[i] == pre_dep:
      pre_dep = li[i]
      dep_measure.append("same as before")
  return dep_measure.count("increased")

depth_measure(depth_list)
