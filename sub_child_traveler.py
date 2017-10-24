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
from edge import Edge

class SubChildTraveler():
	
	def __init__(self, edge_seq, graph):
		self.edge_seq = edge_seq
		self.graph = graph
		self.child_edge = []
	
	def traveler(self):
		self.next_ = len(self.edge_seq) + 1
		#~ size = len(self.graph.get_node_labels())
		size = len(self.graph.get_node_labels())
		self.g2s = []
		self.s2g = []
		self.f = []
		
		i = 0
		while i < size:
			self.g2s.append(-1)
			self.s2g.append(-1)
			self.f.append([])
			j = 0 
			while j < size:
				self.f[i].append(False)
				j += 1
			i += 1
		
		self.rm = []
		i = 0
		while i < size + 1:
			self.rm.append(-1)
			i += 1
		
		for e in self.edge_seq:
			if e.ix < e.iy and e.iy > self.rm[e.ix]:
				self.rm[e.ix] = e.iy
		
		i = 0
		while i < size:
			if self.edge_seq[0].x is not self.graph.get_node_labels()[i]:
				i += 1
				continue
				
			self.g2s[i] = 0
			self.s2g[0] = i
			self.dfs_search_edge(0)
			self.g2s[i] = -1
			self.s2g[0] = -1
			i += 1
	
	def dfs_search_traveler(current_position):
		rm_position = 0
		if current_position >= len(self.edge_seq):
			while rm_position >= 0:
				gid = self.s2g[rm_position]
				
				i = 0
				while i < len(self.graph.get_edge_nexts()[gid]):
					gid2 = self.graph.get_edge_nexts()[gid][i]
					if self.f[gid][gid2] or self.f[gid2][gid]:
						i += 1
						continue
					if self.g2s[gid2] < 0:
						self.g2s[gid2] = self.next_
						e = Edge(self.g2s[gid], self.g2s[gid2], self.graph.get_node_labels()[gid],
							self.graph.get_edge_labels()[gid][i], self.graph.get_node_labels()[gid2])
						self.child_edge.append(e)
						i += 1
					else:
						flag = True 
						j = 0
						while j < len(self.graph.get_edge_nexts()[gid2]):
							temp_id = self.graph.get_edge_nexts()[gid2][j]
							if self.g2s[gid2] < self.g2s[temp_id]:
								flag = False
								break
							j += 1
						if flag:
							e = Edge(self.g2s[gid], self.g2s[gid2], self.graph.get_node_labels()[gid],
								self.graph.get_edge_labels()[gid][i], self.graph.get_node_labels()[gid2])
							self.child_edge.append(e)
						
						i += 1
				rm_position = self.rm[rm_position]
			return
			
			# 如果不是最后一个
			e = self.edge_seq[current_position]
			y = e.y
			a = e.a
			gid1 = s2g[e.ix]
			gid2 = 0
			
			i = 0
			while i < len(self.graph.get_edge_labels()[gid1]):
				if self.graph.get_edge_labels[gid1][i] is not a:
					i += 1
					continue
				temp_id = self.graph.get_edge_nexts[gid1][i]
				if self.graph.get_node_labels[temp_id] is not y:
					i += 1
					continue 
				gid2 = temp_id
				
				if self.g2s[gid2] == -1 and self.s2g[e.iy] == -1:
					self.g2s[gid2] = e.iy
					self.s2g[e.iy] = gid2
					self.f[gid2][gid1] = True
					self.f[gid1][gid2] = True
					self.dfs_search_traveler(current_position + 1)
					self.f[gid1][gid2] = False
					self.f[gid2][gid1] = False
					self.g2s[gid2] = -1
					self.s2g[e.iy] = -1
					i += 1
				else:
					if self.g2s[gid2] is not e.iy or self.s2g[e.iy] is not gid2:
						i += 1
						continue
					self.f[gid2][gid1] = True
					self.f[gid1][gid2] = True
					self.dfs_search_traveler(current_position)
					self.f[gid1][gid2] = False
					self.f[gid2][gid1] = False
					i += 1
			
		
