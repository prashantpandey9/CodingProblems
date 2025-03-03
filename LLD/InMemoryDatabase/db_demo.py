from in_memory_database import InMemoryDatabase

db = InMemoryDatabase()

# Set and get values
db.set('user1', {'name': 'Alice', 'age': 25})
db.set('user2', {'name': 'Bob', 'age': 30})
print(db.get('user1'))  # Output: {'name': 'Alice', 'age': 25}

# Query values
results = db.query(lambda v: v['age'] > 20)
print(results)  # Output: {'user1': {...}, 'user2': {...}}

# Delete values
db.delete('user1')
print(db.get('user1'))  # Output: None