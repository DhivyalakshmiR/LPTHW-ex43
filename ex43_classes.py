#This process is a guide for building things in Python using object-oriented programming #(OOP). It's a flexible set of steps, not strict rules, meant to help with various #programming problems. The steps are:
#   1.	Write a problem.
#   2.	Draw a flow chart of the problem.
#   3.	List all variables, data, other objects and add comments.
#   4.	Build the classes and object map for the problem.
#   5.	Rewrite and refine.

# Create a class hierarchy and object map for the concepts:
# *Map
	#--next_scene
	#--opening_scene
# *Engine
	#--play
# *Scene
	#--enter
	#*Death
	#*Central Corridor
	#*Laser Weapon Armory
	#*The Bridge
	#*Escape Pod

class Scene(object):

	def enter(self):
		pass
		
class Engine(object):

	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass
		
class Death(Scene):

	def enter(self):
		pass
		
class CentralCorridor(Scene):

	def enter(self):
		pass
		
class LaserWeaponArmory(Scene):

	def enter(self):
		pass
		
class TheBridge(Scene):

	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
class Map(object):

	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def openining_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
