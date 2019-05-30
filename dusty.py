#!/usr/bin/python

def main():
	#open text file 
	with open("input.txt") as f:
		#read first line for room dimensions
		content = f.readlines()

	def get_coords(content):
		coords = content.split()
		x = int(coords[0])
		y = int(coords[1])

		return (x,y)

	#get room size and starting point
	room = get_coords(content[0])
	current_point = get_coords(content[1])

	#read subsequent lines for dirt patches
	dirt_patches = {}
	for dirt in content[2:-1]:
		dirt_patches[get_coords(dirt)] = 'dirty'

	#get last line for directions 
	directions = content[-1]

	#start counting dirt patches cleaned
	dirt_cleaned = 0
	
	#method to check if patch is dirty
	def clean_pos(current_point, dirt_patches):
		if current_point in dirt_patches:
			del dirt_patches[current_point]
			return True
		else:
			return False
		
	#method to check if dusty is in the room
	def is_in_room(current_point, room):
		if (0 < current_point[0] <= room[0]) & (0 <current_point[1] <= room[1]):
			return True
		else: 
			return False

	#read first letter of direction, move dusty, check if dirty
	for letter in directions:
		if clean_pos(current_point, dirt_patches) == True:
			dirt_cleaned += 1
		if letter == 'N':
			new_pos = (current_point[0], current_point[1]+1)
		elif letter == 'S':
			new_pos = (current_point[0], current_point[1]-1)
		elif letter == 'W':
			new_pos = (current_point[0]-1, current_point[1])
		elif letter == 'E':
			new_pos = (current_point[0]+1, current_point[1])
		if is_in_room(new_pos, room) == True:	
			current_point = new_pos	
		if clean_pos(current_point, dirt_patches) == True:
			dirt_cleaned += 1

	print current_point
	print dirt_cleaned



if __name__ == '__main__':
	main()
