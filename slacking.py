import pyautogui as gui
from sys import argv
from time import sleep
from random import randrange
from string import ascii_letters, punctuation


SCREEN_RESOLUTION: list[int] = gui.size()
SCREEN_WIDTH: int = SCREEN_RESOLUTION[0]
SCREEN_HEIGHT: int = SCREEN_RESOLUTION[1]
ONE_MINUTE_IN_SECONDS = 60
ONE_SIXTH_OF_A_MINUTE = 10


def moveMouseToRandomPos():
	gui.moveTo(randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT), 0.5, gui.easeInOutQuad)
	gui.moveTo(randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT), 0.5, gui.easeInOutQuad)

def altTab(tabPressCount: int):
	tabPressQueue: list[str] = ['tab' for i in range(tabPressCount)]
	with gui.hold('command') or gui.hold('tab'):
		gui.press(tabPressQueue)

def stopSlacking():
	gui.FAILSAFE = True
	gui.moveTo(0, 0)


def calculateMinutes() -> int:
	inputCount = len(argv)
	if inputCount > 4:
		raise IndexError('too many arguments were provided')

	if inputCount < 2:
		minutes = 5
		return minutes

	inputs: list[str] = argv
	inputs.reverse()
	inputs.pop()

	if inputCount >= 2:
		nonDigitChars: str = ascii_letters + punctuation
		minutes = evalMinutesInput(inputs.pop(), nonDigitChars)

		if inputCount >= 3:
			gui.FAILSAFE = evalFailSafeInput(inputs.pop())
			
			if inputCount == 4:
				gui.PAUSE = evalPauseInput(inputs.pop(), nonDigitChars)

	return minutes

def evalMinutesInput(userInput: str, invalidInput: str) -> int:
	minutesInput = int(userInput)
	if minutesInput <= 0:
		raise ValueError('the first argument input must be greater than 0')
	elif len(set(userInput).intersection(invalidInput)) > 0:
		raise ValueError('the first argument input must be an integer')
	else:
		return minutesInput
	
def evalFailSafeInput(userInput: str) -> bool:
	if not userInput in ['y', 'n']:
		raise ValueError("the second argument input must be a string value of either 'y' or 'n'")
	elif userInput == 'y':
		print('Fail-safe is on')
		return True
	elif userInput == 'n':
		print('Fail-safe is off')
		return False
	
def evalPauseInput(userInput: str, invalidInput: str) -> float:
	invalidInput = invalidInput.replace('.', '')
	if float(userInput) <= 0:
		raise ValueError('the third argument input must be greater than 0')
	elif len(set(userInput).intersection(invalidInput)) > 0:
		raise ValueError('the third argument input must be an int or float')
	else:
		print(f'Pause time set to {userInput}')
		return float(userInput)


def main():
	try:
		print('Press Ctrl-C to quit.')
		numMinutes: int = calculateMinutes()
		print(f'Slack for {numMinutes} minute(s)...')
			
		for i in range(numMinutes * ONE_SIXTH_OF_A_MINUTE):
			moveMouseToRandomPos()
			sleep(ONE_MINUTE_IN_SECONDS / ONE_SIXTH_OF_A_MINUTE)
	except KeyboardInterrupt:
		print('\r')


if __name__ == '__main__':
	main()
