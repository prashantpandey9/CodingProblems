import unittest
from in_memory_database import InMemoryDatabase

class TestInMemoryDatabase(unittest.TestCase):
    def setUp(self):
        """Setup a fresh database for each test."""
        self.db = InMemoryDatabase()

    def test_set_and_get(self):
        """Test basic set and get functionality."""
        self.db.set("key1", "value1")
        self.assertEqual(self.db.get("key1"), "value1")

    def test_get_nonexistent_key(self):
        """Test getting a nonexistent key returns None."""
        self.assertIsNone(self.db.get("nonexistent_key"))

    def test_delete_key(self):
        """Test deleting an existing key."""
        self.db.set("key1", "value1")
        self.db.delete("key1")
        self.assertIsNone(self.db.get("key1"))

    def test_delete_nonexistent_key(self):
        """Test deleting a nonexistent key raises an error."""
        with self.assertRaises(ValueError):
            self.db.delete("nonexistent_key")

if __name__ == "__main__":
    unittest.main()
