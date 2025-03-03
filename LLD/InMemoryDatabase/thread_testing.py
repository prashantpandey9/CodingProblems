import threading
from in_memory_database import InMemoryDatabase

# Create the database instance
db = InMemoryDatabase()

def writer():
    for i in range(5):
        db.set(f"key{i}", f"value{i}")

def reader():
    for i in range(5):
        print(db.get(f"key{i}"))

# Create threads for simultaneous reading and writing
write_thread = threading.Thread(target=writer)
read_thread = threading.Thread(target=reader)

# Start the threads
write_thread.start()
read_thread.start()

# Wait for both threads to finish
write_thread.join()
read_thread.join()

# Print final data
print(db.data_store.store)
