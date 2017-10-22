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

class EdgeFreqency():
	
	def __init__(self, node_label_num, edge_label_num):
		self.node_label_num = node_label_num
		self.edge_label_num = edge_label_num
		self.edge_freq_count = []
		print('self')
		print(self.node_label_num)
		print(self.edge_label_num)
		i = 0
		j = 0
		k = 0
		while i < self.node_label_num:
			self.edge_freq_count.append([])
			j = 0
			while j < self.edge_label_num:
				self.edge_freq_count[i].append([])
				k = 0
				while k < self.node_label_num:
					#~ pdb.set_trace()
					self.edge_freq_count[i][j].append(0)
					k += 1
				j += 1
			i += 1
	
	def print_edge(self):
		print('edge_freq')
		print(self.edge_freq_count)
