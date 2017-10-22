#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  for_test.py
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
from graph_data import GraphData
import pdb

class Graph():
	
	def __init__(self):
		self.node_labels = []
		self.edge_labels = []
		self.edge_nexts = []
	
	def get_node_labels(self):
		return self.node_labels
	
	def get_edge_labels(self):
		return self.edge_labels
	
	def get_edge_nexts(self):
		return self.edge_nexts
	
	def print_graph(self):
		print('print graph')
		print(self.node_labels)
		print(self.edge_labels)
		print(self.edge_nexts)
		
	
	def construct_graph(self, gd):
		
		i = 0
		while i < len(gd.node_labels):
			if gd.node_visibles[i]:
				self.node_labels.append(gd.node_labels[i])
				self.edge_labels.append([])
				self.edge_nexts.append([])
			i += 1
		
		i = 0 
		while i < len(gd.edge_labels):
			if gd.edge_visibles[i]:
				self.edge_labels[gd.edge_x[i]].append(gd.edge_labels[i])
				self.edge_labels[gd.edge_y[i]].append(gd.edge_labels[i])
				self.edge_nexts[gd.edge_x[i]].append(gd.edge_y[i])
				self.edge_nexts[gd.edge_y[i]].append(gd.edge_x[i])
			i += 1
		
		self.print_graph()
	
	def has_edge(self, x, a, y):
		is_contained = False
		x = str(x)
		a = str(a)
		y = str(y)
		t = -1
		i = 0
		while i < len(self.node_labels):
			if self.node_labels[i] == x:
				#~ print(self.node_labels[i])
				#~ pdb.set_trace()
				t = y
			elif self.node_labels[i] == y:
				t = x
			else:
				i += 1
				continue
			#~ pdb.set_trace()
			j = 0
			while j < len(self.edge_labels[i]):
				if self.edge_labels[i][j] == a and self.node_labels[self.edge_nexts[i][j]]== t:
					#~ pdb.set_trace()
					is_contained = True
					return is_contained
				j += 1
			i += 1
		#~ print('end graph')
		return is_contained
		
		
				
		
