import sys
import unittest
from cartoon_collections import roll_call_dwarves, summon_captain_planet, long_planeteer_calls, find_the_cheese

class CartoonTest(unittest.TestCase):

  def setUp(self):
    pass

  def test_roll_call_dwarves(self):
    # it prints out the 7 dwarfs in a numbered list
      dwarves = ["Dopey", "Grumpy", "Bashful"]
      roll_call_dwarves(dwarves)
      if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
      output = sys.stdout.getvalue().strip()
      
      # This regex allows for arbitrary characters between
      # the numbering and the name
      self.assertRegexpMatches(output, r'1.*Dopey')
      self.assertRegexpMatches(output, r'2.*Grumpy')
      self.assertRegexpMatches(output, r'3.*Bashful')

  def test_summon_captain_planet(self):
    # returns an array with the same number of elements that it was given
      veggies = 'carrot cucumber pepper'.split()
      result = summon_captain_planet(veggies)
      # self.assertTrue(result is list)
      self.assertEqual(len(result), 3)

    # capitalizes each element and adds an exclamation mark
      fruits = 'apple banana orange'.split()
      result = summon_captain_planet(fruits)
      for item in ['Apple!', 'Banana!', 'Orange!']:
          self.assertTrue(item in result)

      veggies = 'carrot cucumber pepper'.split()
      result = summon_captain_planet(veggies)
      for veggie in ["Carrot!", "Cucumber!", "Pepper!"]:
          self.assertTrue(veggie in result)

  def test_long_planeteer_calls(self):
    # are any calls in the list longer than 4 characters? Yes.
      test_calls = 'earth wind fire water heart'.split()
      self.assertTrue(long_planeteer_calls(test_calls))

      short_calls = 'wind fire'
      self.assertFalse(long_planeteer_calls(short_calls))

  def test_find_the_cheese(self):
    # finds the CHEEeeeEEEeeeSSEEE
      cheddar_cheese = 'banana cheddar sock'.split()
      self.assertEqual(find_the_cheese(cheddar_cheese), 'cheddar')

      no_cheese = 'ham cellphone computer'.split()
      self.assertIsNone(find_the_cheese(no_cheese))

      camembert_cheese = 'owl blanket camembert'.split()
      self.assertEqual(find_the_cheese(camembert_cheese),'camembert')

      gouda_cheese = 'gouda cheddar camembert pontoons'.split()
      self.assertEqual(find_the_cheese(gouda_cheese),'gouda')

if __name__ == '__main__':
    unittest.main()