#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graph_data.py
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


class GraphData():
	"""存储图的原始数据"""
	
	def __init__(self):
		self.node_labels = [] #节点标签
		self.node_visibles = [] #节点是否可见
		self.edge_labels = [] # 边标签
		self.edge_visibles = [] # 边是否可见
		self.edge_x = [] # 边的一端节点的id，from节点
		self.edge_y = [] # 边的另一端节点的id，to节点
	
	def set_node_labels(self, node_labels):
		self.node_labels = node_labels
	
	def get_node_labels(self):
		return self.node_labels
	
	def set_node_visibles(self, node_visibles):
		self.node_visibles = node_visibles
	
	def get_node_visibles(self):
		return self.node_visibles
	
	def set_edge_labels(self, edge_labels):
		self.edge_labels = edge_labels
	
	def get_edge_labels(self):
		return self.edge_labels
	
	def set_edge_visibles(self, edge_visibles):
		self.edge_visibles = edge_visibles
	
	def get_edge_visibles(self):
		return self.edge_visibles
	
	def set_edge_x(self, edge_x):
		self.edge_x = edge_x
	
	def get_edge_x(self):
		return self.edge_x
	
	def set_edge_y(self, edge_y):
		self.edge_y = edge_y
	
	def get_edge_y(self):
		return self.edge_y
	
	def print_graph_data(self):
		print(self.node_labels)
		print(self.node_visibles)
		print(self.edge_labels)
		print(self.edge_visibles)
		print(self.edge_x)
		print(self.edge_y)
	
	def remove_infreq_nodes_and_edges(self, freq_node_label, 
		freq_edge_label, min_support):
		
		i = 0
		for node_label in self.node_labels:
			label = int(node_label)
			if freq_node_label[label] < min_support:
				#~ print('make false')
				#~ print(label)
				#~ print(freq_node_label[label])
				self.node_visibles[i] = False
			i += 1
		
		i = 0
		for edge_label in self.node_labels:
			#~ print(edge_label)
			label = int(edge_label)
			if freq_edge_label[label] < min_support:
				#~ print('make false')
				#~ print(label)
				#~ print(freq_edge_label[label])
				self.edge_visibles[i] = False
			x = self.edge_x[i]
			y = self.edge_y[i]
			if not self.node_visibles[x] or not self.node_visibles[y]:
				self.edge_visibles[i] = False
			i += 1
			
	
	


#~ gd = GrapData()
