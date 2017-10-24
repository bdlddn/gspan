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
from edge import Edge
import pdb

class DfsCodeTraveler():
	
	def __init__(self, edge_seq, graph):
		self.is_min = True
		self.edge_seq = edge_seq # 当前挖掘的图的五元组编码
		self.graph = graph # 当前的图结构
		self.g2s = [] #	图节点对应的边五元组id标识
	
	def traveler(self):
		node_num = len(self.graph.get_node_labels())
		i = 0
		while i < node_num:
			self.g2s.append(-1)
			i += 1
		
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
			if int(self.graph.get_node_labels()[i]) > int(self.edge_seq[0].x):
				# 可能要加int转换
				i += 1
				continue
			self.g2s[i] = 0
			s = []
			s.append(i)
			self.dfs_search(s, 0, 1)
			if not self.is_min:
				return
			self.g2s[i] = -1
			i += 1
		
	
	def dfs_search(self, s, current_position, next_):
		if current_position >= len(self.edge_seq):
			s.pop()
			return
		
		while len(s) > 0:
			x = s.pop()
			i = 0 
			while i < len(self.graph.get_edge_nexts()[x]):
				#~ pdb.set_trace()
				y = self.graph.get_edge_nexts()[x][i]
				if self.f[x][y] or self.f[y][x]:
					i += 1
					continue
				#  如果节点没有被使用过
				if  self.g2s[y] < 0:
					e = Edge(self.g2s[x], next_, self.graph.get_node_labels()[x],
						self.graph.get_edge_labels()[x][i], self.graph.get_node_labels()[y])
				
					compare_result = e.compare_with(self.edge_seq[current_position])
				
					if compare_result == e.edge_smaller:
						self.is_min = False
						return
					elif compare_result == e.edge_larger:
						i += 1
						continue
					# 相等则继续比较
					self.g2s[y] = next_
					self.f[x][y] = True
					self.f[y][x] = True
					s.append(y)
					self.dfs_search(s, current_position + 1, next_ + 1)
					if not self.is_min:
						return
					else:
						self.f[x][y] = False
						self.f[y][x] = False
						self.g2s[y] = -1
						i += 1
				# 如果节点有被使用过
				else:
					e = Edge(self.g2s[x], self.g2s[y], self.graph.get_node_labels()[x],
						self.get_edge_labels()[x][i], self.get_node_labels()[y])
					compare_result = e.compare_with(self.edge_seq[current_position])
					
					if compare_result == e.edge_smaller:
						self.is_min = False
						return
					elif compare_result == e.edge_larger:
						i += 1
						continue
					g2s[y] = self.next_
					self.f[x][y] = True
					self.f[y][x] = True
					s.push(y)
					self.dfs_search(s, current_position + 1, next_)
					if not self.is_min:
						return
					self.f[x][y] = True
					self.f[y][x] = True
					i += 1
					
