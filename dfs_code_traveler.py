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
#~ from graph_data import GraphData
from graph import Graph

class DfsCodeTraveler():
	
	def __init___(self):
		self.is_min = True
		self.edge_seq = [] # 当前挖掘的图的五元组编码
		self.graph = Graph() # 当前的图结构
		self.g2s = [] #	图节点对应的边五元组id标识
	
	def traveler(self):
		node_num = len(graph.get_node_labels())
		i = 0
		while i < node_num:
			self.g2s[i] = -1
		
		self.f = []
		
		i = 0
		while i < node_num:
			self.f.append([])
			j = 0
			while j < node_num:
				self.f[i].append(False)
				j += 1
			i += 1
		
		i = 0
		while i < node_num:
			if self.graph.get_node_labels()[i] > self.edge_seq[0].x:
				# 可能要加int转换
				i += 1
				continue
			self.g2s[i] = 0
			s = []
			s.push(i)
			dfs_search(s, 0, 1)
			if not self.is_min:
				return
			self.g2s[i] = -1
			i += 1
		
		
