#!/usr/bin/env python

tree_list = ['oak', 'hickory', 'pecan']
print('tree_list is: ', tree_list)

del tree_list[:]
print('tree_list is now empty: ', tree_list)

tree_list_copy = tree_list
print('tree_list_copy is empty too: ', tree_list_copy)

tree_list[:] = ['maple', 'birch', 'apple']
print('tree_list is now: ', tree_list)
print('and so is tree_list_copy: ', tree_list_copy)

print('tree_list_copy is a full copy? ', tree_list_copy is tree_list)

shallow_copy = tree_list[:]
print('shallow_copy is a shallow copy? ', shallow_copy is tree_list)
