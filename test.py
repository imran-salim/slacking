import unittest
from string import ascii_letters, digits, punctuation

from slacking import evalMinutesInput, evalFailSafeInput, evalPauseInput


class TestUserInput(unittest.TestCase):
  
  def testMinutesInput(self):
    validInputs = ['10', '1', '20']
    invalidInputs = ['-5', '2.5'] + [l for l in ascii_letters] + [p for p in punctuation]
    nonDigitChars = ascii_letters + punctuation

    for i in validInputs:
      self.assertEqual(evalMinutesInput(i, nonDigitChars), int(i))

    for i in invalidInputs:
      with self.assertRaises(ValueError):
        evalMinutesInput(i, nonDigitChars)

  def testFailSafeInput(self):
    invalidInputs = ascii_letters + digits + punctuation
    invalidInputs = invalidInputs.replace('y', '')
    invalidInputs = invalidInputs.replace('n', '')
      
    self.assertTrue(evalFailSafeInput('y'))
    self.assertFalse(evalFailSafeInput('n'))

    for i in invalidInputs:
      with self.assertRaises(ValueError):
        evalFailSafeInput(i)

  def testPauseInput(self):
    validInputs = ['0.1', '1', '5.0', '10.001']
    invalidInputs = [l for l in ascii_letters] + [p for p in punctuation] + ['0', '-1', '-5.0', '-10.001']
    nonDigitChars = ascii_letters + punctuation

    for i in validInputs:
      self.assertEqual(evalPauseInput(i, nonDigitChars), float(i))

    for i in invalidInputs:
      with self.assertRaises(ValueError):
        evalPauseInput(i, nonDigitChars)


if __name__ == '__main__':
  unittest.main()
