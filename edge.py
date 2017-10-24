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

class Edge():
	
	def __init__(self, ix, iy, x, a, y):
		self.edge_equal = 0
		self.edge_smaller = 1
		self.edge_larger = 2
		self.ix = ix
		self.iy = iy
		self.x = x
		self.a = a
		self.y = y
	
	def compare_with(self, e):
		result = self.edge_equal
		array1 = [self.ix, self.iy, self.x, self.y, self.a]
		array2 = [e.ix, e.iy, e.x, e.y, e.a]
		
		i = 0
		while i < len(array1):
			if array1[i] < array2[i]:
				result = self.edge_smaller
				break
			elif array1[i] > array2[i]:
				result = self.edge_larger
				break
			else:
				i += 1
				continue
		
		return result 
	
	def print_edge(self):
		print(self.ix, self.iy, self.x, self.y, self.a)
				
		
				
		
