## Project Overview

This project demonstrates fundamental NoSQL database operations using MongoDB, covering both MongoDB shell commands and Python interactions through PyMongo. It includes CRUD operations, document management, and log analysis.

## Key Features

- **MongoDB Shell Operations**:
  - Database listing and creation
  - Document insertion, querying, updating, and deletion
  - Basic aggregation and counting

- **Python/PyMongo Implementations**:
  - Document listing and insertion
  - Bulk updates and topic-based queries
  - Nginx log statistics analysis

- **Advanced Operations**:
  - Field updates with new attributes
  - Topic-based document filtering
  - Log analysis with method statistics

## Technical Requirements

- MongoDB 4.2
- Python 3.7
- PyMongo 3.10
- Ubuntu 18.04 LTS

## Installation & Setup

1. Install MongoDB:
```bash
sudo apt-get install -y mongodb-org
```

2. Install PyMongo:
```bash
pip3 install pymongo
```

3. Import sample data (for log analysis):
```bash
mongorestore dump
```

## Project Structure

| File | Description |
|------|-------------|
| `0-list_databases` | Lists all MongoDB databases |
| `1-use_or_create_database` | Creates/uses specified database |
| `2-insert` | Inserts document into collection |
| `3-all` | Lists all documents in collection |
| ... | ... |
| `12-log_stats.py` | Analyzes Nginx log statistics |

## Usage Examples

**Basic MongoDB operations:**
```bash
./3-all | mongo my_db
```

**Python implementations:**
```bash
./11-main.py
```

**Log analysis:**
```bash
./12-log_stats.py
```

## Learning Outcomes

- Understanding NoSQL vs SQL differences
- Implementing ACID concepts in NoSQL
- Performing CRUD operations in MongoDB
- Working with document storage and collections
- Analyzing database content programmatically