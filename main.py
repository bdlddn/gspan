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
import pdb
from graph_data import GraphData
from graph import Graph
from edge_freqency import EdgeFreqency
from edge import Edge
from graph_code import GraphCode
from dfs_code_traveler import DfsCodeTraveler
from sub_child_traveler import SubChildTraveler
import datetime

#  定义全局变量
min_support = 300
input_data_path = './graph.data'
label_max = 100
data_array = []
freq_node_label = []
freq_edge_label = []
total_graph_data = []
input_new_graph = 't'
input_vertice = 'v'
input_edge = 'e'
new_node_label_count = 0
new_edge_label_count = 0
result_graph = []
total_graph = []


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
			rank_node_labels[k] = rank_node_labels[i]
			rank_node_labels[i] = temp
		i += 1
	
	# 数组中[i]=j表示排名第i的边的标号是j
	i = 0
	while i < label_max - 1:
		k = 0
		label1 = rank_edge_labels[i]
		temp = label1
		j = i + 1
		while j < label_max:
			label2 = rank_edge_labels[j]
			if freq_edge_label[temp] < freq_edge_label[label2]:
				temp = label2
				k = j
			j += 1
		if label1 != temp:
			temp = rank_edge_labels[k]
			rank_edge_labels[k] = rank_edge_labels[i]
			rank_edge_labels[i] = temp
		i += 1
	
	i = 0
	while i < label_max:
		node_labels_2_rank.append(-1)
		edge_labels_2_rank.append(-1)
		i += 1
	
	# 数组[i] = j表示标号为i的节点排名为j
	i = 0
	while i < label_max:
		node_labels_2_rank[rank_node_labels[i]] = i
		i += 1
	
	# 数组[i] = j表示标号为i的边排名为j
	i = 0
	while i < label_max:
		edge_labels_2_rank[rank_edge_labels[i]] = i
		i += 1
	
	# 调用graph_data中的方法按照标号-排名进行重新排列
	for gd in total_graph_data:
		gd.relabel_by_rank(node_labels_2_rank, edge_labels_2_rank)
	
	global new_node_label_count
	global new_edge_label_count
	for label in rank_node_labels:
		if freq_node_label[int(label)] < min_support:
			break
		new_node_label_count += 1 # 全局变量只能赋值？
	
	for label in rank_edge_labels:
		if freq_edge_label[int(label)] < min_support:
			break
		new_edge_label_count += 1

	
def sub_mining(gc, next_):
	"""开始进行子图挖掘"""	
	# 首先根据gc中的五元组来构造图
	graph = Graph()
	
	i = 0
	while i < next_:
		graph.get_node_labels().append(-1)
		graph.get_edge_labels().append([])
		graph.get_edge_nexts().append([])
		i += 1
	
	i = 0
	while i < len(gc.get_edge_seq()):
		e = gc.get_edge_seq()[i]
		id1 = e.ix
		id2 = e.iy
		graph.get_node_labels()[id1] = e.x
		graph.get_node_labels()[id2] = e.y
		graph.get_edge_labels()[id1].append(e.a)
		graph.get_edge_labels()[id2].append(e.a)
		graph.get_edge_nexts()[id1].append(id2)
		graph.get_edge_nexts()[id2].append(id1)
		i += 1
	
	# 看看是否是最小dfs—code
	d_traveler = DfsCodeTraveler(gc.get_edge_seq(), graph)
	d_traveler.traveler()
	if not d_traveler.is_min:
		return
	result_graph.append(graph)
	
	# 进行子图挖掘
	g_ids = []
	edge_2_gid = {}
	for i in range(0,len(gc.get_gs())):
		id_ = gc.get_gs()[i]
		sct = SubChildTraveler(gc.get_edge_seq(), total_graph[id_])
		sct.traveler()
		edge_array = sct.child_edge
		for e2 in edge_array:
			if not edge_2_gid.has_key(e2):
				gids = []
			else:
				gids = edge_2_gid[e2]
			gids.append(id_)
			edge_2_gid[e2] = gids
	
	for key, value in edge_2_gid.items():
		e1 = key
		gids = value
		if len(gids) < min_support:
			continue
		ngc = GraphCode()
		for edge in gc.get_edge_seq():
			ngc.get_edge_seq().append(edge)
		ngc.get_edge_seq().append(e1)
		for gid in gids:
			ngc.get_gs().append(gid)
		if e1.iy == next_:
			sub_mining(ngc, next_ + 1)
		else:
			sub_mining(ngc, next_)
		
	
	
	
def freq_graph_mining():
	"""开始进行频繁模式挖掘"""
	
	
	
	for gd in total_graph_data:
		g = Graph()
		g.construct_graph(gd)
		total_graph.append(g)
	
	ef = EdgeFreqency(new_node_label_count, new_edge_label_count)
	i = 0
	while i < new_node_label_count:
		j = 0
		while j < new_edge_label_count:
			k = 0
			while k < new_node_label_count:
				for g in total_graph:
					if g.has_edge(i, j, k):
						ef.edge_freq_count[i][j][k] += 1
				k += 1
			j += 1
		i += 1
	#~ ef.print_edge()
	
	i = 0 
	while i < new_node_label_count:
		j = 0
		while j < new_edge_label_count:
			k = 0
			while k < new_node_label_count:
				if ef.edge_freq_count[i][j][k] >= min_support:
					gc = GraphCode()
					edge = Edge(0, 1, i, j, k)
					gc.get_edge_seq().append(edge)
					
					y = 0
					for g in total_graph:
						if g.has_edge(i, j, k):
							gc.get_gs().append(y)
						y += 1
					sub_mining(gc, 2)
				k += 1
			j += 1
		i += 1
		



if __name__ == "__main__":
	#从文件读取数据到data_array数组
	with open(input_data_path) as file_object:
		for line in file_object:
			data_array.append(line.replace('\n','').split(' '))
	
	#  设置开始时间
	start_time = datetime.datetime.now()
	
	# 统计每一个边和点的出现次数，并将data_array中的数据加入到data_graph中
	i = 0
	while i < label_max:
		freq_edge_label.append(0)
		freq_node_label.append(0)
		i += 1
	
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
	#排序并重新标号
	sort_and_relabel()
	
	#  进行频繁子图挖掘
	freq_graph_mining()
	
	# 结束时间
	end_time = datetime.datetime.now()
	
	print('run time:')
	print(end_time - start_time)
	print('total result graph number')
	print(len(result_graph))
	
	
	
	
		
