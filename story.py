import subprocess

from stories import *

def story():
	active = True
	while active:
		print("Introduction")
		intro_input = raw_input("If you choose the forest, type in 'left' or 'l' or to continue alongside the sea, type 'right' or 'r': ")
		if intro_input == "left" or intro_input == "l":
			print("Forest option text")
			forest_input = raw_input("Type 'reveal' or 'r' to reveal the shadow or 'walk' or 'w' to continue walking: ")
			if forest_input == "r" or forest_input == "reveal":
				print("reveal-shadow")
				wizard_input == raw_input("Type 'r'/'run' to run from the wizard or 'f'/'face' to face it: ")
				if wizard_input == "face" or "f":
					print("Face wizard text")
					riddle_input = raw_input("Type your answer here ")
					if riddle_input == "steps" or ridde_input == "footsteps":
						print("correct-answer-conclusion")
						active = False
					elif riddle_input = "h" or riddle_input == "hint"
						print("hint-riddle ")
						riddle_input = raw_input("Type your answer here ")
						if riddle_input == "steps" or ridde_input == "footsteps":
							print("correct-answer-conclusion")
							active = False
					else:
						print("Wizard attack")
						active = False
			else: 
				print("Shadow attack and die")
				active = False
		elif intro_input == "right" or intro_input == "r":
			print("Sea option text")
			sea_input = raw_input("Type 'w' or 'water' to go into the water or 'l' or 'land' to get out: ")
			if sea_input == "l" or sea_input == "land":
				print("run to land")
				wizard_input == raw_input("Type 'r'/'run' to run from the wizard or 'f'/'face' to face it: ")
				if wizard_input == "face" or "f":
					print("Face wizard text")
					riddle_input = raw_input("Type your answer here ")
					if riddle_input == "steps" or ridde_input == "footsteps":
						print("correct-answer-conclusion")
						active = False
					elif riddle_input = "h" or riddle_input == "hint"
						print("hint-riddle ")
						riddle_input = raw_input("Type your answer here ")
						if riddle_input == "steps" or ridde_input == "footsteps":
							print("correct-answer-conclusion")
							active = False
					else:
						print("Wizard attack")
						active = False
			else:
				print("Water demon attack")
				active = False
		else:
			active = False


def main():
	f = open("stories/intro.txt", "r")
	introduction = f.read()
	f.close()
	story()

	with open('stories/intro.txt', 'r') as f:
     	story_content['intro'] = f.read()


if __name__ == '__main__':
	main()