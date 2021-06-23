import unittest
from world import World

class TestWorld(unittest.TestCase):
	def test_constructor(self):
		# Non-argument constructor is working
		w = World()
		self.assertEqual(w.world, 'Earth')

		# Argument constructor is working
		sw = World("Mars")
		self.assertEqual(sw.world, 'Mars')

		# Wrong argument raising exception
		with self.assertRaises(ValueError) as error:
			wrong_world = World("sun")
		self.assertEqual(str(error.exception), "Don't known planet Sun!")


	def test_validator(self):
		w = World()
		planets = ['Merkury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Ceres','Pluto','Haumea','Makemake','Eris']
		
		# Check if all planets from the list will be correctly validated 
		for planet in planets:
			self.assertTrue(w.validate(planet))
		
		# Check that empty value will be invalidated
		self.assertFalse(w.validate(None))
		
		# Check if wrong value will be invalidated
		self.assertFalse(w.validate("Sun"))

		# Check if not normalized value will be invalidated (expected)
		self.assertFalse(w.validate("merkury"))

	def test_normalizer(self):
		w = World()
		self.assertEqual(w.normalize("mars"), "Mars")
		self.assertEqual(w.normalize("MARS"), "Mars")
		self.assertEqual(w.normalize("mARS"), "Mars")
		self.assertEqual(w.normalize("Mars"), "Mars")
		self.assertEqual(w.normalize("mArS123"), "Mars123")

	def test_printable_descrition(self):
		w = World()
		aw = World("Jupiter")
		self.assertEqual(str(w), "Hello world!")
		self.assertEqual(str(aw), "Welcome on Jupiter")

if __name__ == '__main__':
	unittest.main()