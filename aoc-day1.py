# Load Data file
import requests
data_url = requests.get("https://adventofcode.com/2021/day/1/input")
depth_reading = data_url.text
depth_list = []
for i, line in enumerate(depth_reading.split('\n')):
  if line != "":
    depth_list.append(int(line))

# Part- 1:
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

# Part- 2:
def sliding_window(li):
  cluster_dep = []
  cluster = []
  tenp_clus = 0
  for i in range(len(li)):
    if i+2 < len(li):
      temp_clus = (li[i]+li[i+1]+li[i+2])
      cluster.append(temp_clus)
  for i in range(len(cluster)):
    if i == 0:
      cluster_dep.append("N/A - no previous measurement")
    elif cluster[i]> cluster[i-1]:
      cluster_dep.append("increased")
    elif cluster[i]> cluster[i-1]:
      cluster_dep.append("decreased")
    elif cluster[i] == cluster[i-1]:
      cluster_dep.append("no change")
  return cluster_dep.count("increased")

sliding_window(depth_list)

