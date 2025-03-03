Designing an in-memory database involves creating a system that stores data in memory rather than persistent storage. This kind of database is optimized for high-speed access and is typically used in scenarios requiring low-latency data retrieval and processing. Here's a low-level design for an in-memory database:


# Core Requirements
### Features
- CRUD Operations: Support Create, Read, Update, and Delete operations.
- Data Structures: Provide basic data structures like key-value pairs, lists, sets, and sorted sets.
- Concurrency: Handle concurrent read and write operations safely.
- Persistence (Optional): Periodic snapshots or logs for backup.
- Query Support: Allow simple queries like filtering and range operations.
- Expiration: Support key expiration for cache use cases.
