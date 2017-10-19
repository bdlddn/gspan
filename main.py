#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2017 masai <masai@masaideMacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

'''主程序的入口'''
import sys
from graph_data import GraphData

min_support = 1
input_data_path = './graph_simple.data'
label_max = 10
data_array = []
freq_node_label = []
freq_edge_label = []
total_graph_data = []
input_new_graph = 't'
input_vertice = 'v'
input_edge = 'e'
min_support = 1

#~ def main(agrs):
	#~ return 0
def sort_and_relabel():
	"""进行排序和重新编号"""
	rank_node_labels = []
	rank_edge_labels = []
	node_labels_2_rank = []
	edge_labels_2_rank = []
	
	i = 0
	while i < label_max:
		rank_node_labels.append(i)
		rank_edge_labels.append(i)
		i += 1
	
	label1 = 0
	lable2 = 0
	tmp = 0
	
	# 数组中[i]=j表示排名第i的节点的标号是j
	i = 0
	while i < label_max - 1:
		k = 0
		label1 = rank_node_labels[i]
		temp = label1
		j = i + 1
		while j < label_max:
			label2 = rank_node_labels[j]
			if freq_node_label[temp] < freq_node_label[label2]:
				temp = label2
				k = j
			j += 1
		if label1 != temp:
			temp = rank_node_labels[k]
			rank_node_labels[i] = rank_node_labels[k]
			rank_node_labels[k] = temp
		i += 1
	
	# 数组中[i]=j表示排名第i的边的标号是j
	i = 0
	while i < label_max - 1:
		k = 0
		label1 = rank_edge_labels[i]
		temp = label1
		j = 0
		while j < label_max:
			label2 = rank_edge_labels[j]
			if freq_edge_label[temp] < freq_edge_label[label2]:
				temp = label2
				k = j
			j += 1
		if label1 != temp:
			temp = rank_node_labels[k]
			rank_node_labels[i] = rank_node_labels[k]
			rank_node_labels[k] = temp
		i += 1
	
	i = 0
	while i < label_max:
		node_labels_2_rank.append(-1)
		edge_labels_2_rank.append(-1)
		i += 1
	
	# 数组[i] = j表示标号为i的节点排名为j
	i = 0
	while i < label_max:
		node_labels_2_rank[rank_edge_labels[i]] = i
		i += 1
	
	# 数组[i] = j表示标号为i的边排名为j
	i = 0
	while i < label_max:
		edge_labels_2_rank[rank_edge_labels[i]] = i
		i += 1
	# 输出看看结果
	print(rank_node_labels)
	print(rank_edge_labels)
	print(node_labels_2_rank)
	print(edge_labels_2_rank)
	print('haha')
	
	
	# 调用graph_data中的方法按照标号-排名进行重新排列
				
	



if __name__ == "__main__":
	#从文件读取数据到data_array数组
	#~ data_array = []
	with open(input_data_path) as file_object:
		#~ contents = file_object.read()
		#~ print(contents)
		for line in file_object:
			data_array.append(line.replace('\n','').split(' '))
	
	# 统计每一个边和点的出现次数，并将data_array中的数据加入到data_graph中
	i = 0
	while i < label_max:
		freq_edge_label.append(0)
		freq_node_label.append(0)
		i += 1
	#~ print(freq_edge_label)
	
	gd = GraphData()
	
	for array in data_array:
		if array[0] == input_new_graph:
			# 有数据时将gd加入到total_graph
			if gd.get_node_labels():
				total_graph_data.append(gd)
			gd = GraphData()
		elif array[0] == input_vertice:
			if not array[2] in gd.get_node_labels():
				freq_node_label[int(array[2])] += 1
			gd.get_node_labels().append(array[2])
			gd.get_node_visibles().append(True)
		
		elif array[0] == input_edge:
			if not array[3] in gd.get_edge_labels():
				#~ temp = freq_edge_label[int(array[3])]
				#~ temp += 1
				freq_edge_label[int(array[3])] += 1
			gd.get_edge_labels().append(array[3])
			gd.get_edge_visibles().append(True)
			gd.get_edge_x().append(int(array[1]))
			gd.get_edge_y().append(int(array[2]))
	
	#  看看graphdata存储是否正确
	#~ for gd in total_graph_data:
		#~ print(gd.print_graph_data())
	#~ print(freq_node_label)
	#~ print(freq_edge_label)
	
	# 移除graph_data中不频繁的边和点
	for gd in total_graph_data:
		gd.remove_infreq_nodes_and_edges(freq_node_label,
			freq_edge_label, min_support)
		#~ gd.print_graph_data()
	#排序并重新标号
	sort_and_relabel()
	
	
	
	
	
		
