# MySQL Advanced Project

This repository contains solutions for the MySQL Advanced project, which covers various advanced MySQL concepts including constraints, indexes, stored procedures, functions, views, and triggers.

## Project Tasks

### 0. We are all unique!
**File:** `0-uniq_users.sql`  
Creates a table `users` with unique email constraints.

### 1. In and not out
**File:** `1-country_users.sql`  
Creates a table `users` with an enumeration for country fields.

### 2. Best band ever!
**File:** `2-fans.sql`  
Ranks country origins of bands by number of fans.

### 3. Old school band
**File:** `3-glam_rock.sql`  
Lists Glam rock bands ranked by longevity.

### 4. Buy buy buy
**File:** `4-store.sql`  
Creates a trigger that decreases item quantity after new orders.

### 5. Email validation to sent
**File:** `5-valid_email.sql`  
Creates a trigger that resets `valid_email` when email is changed.

### 6. Add bonus
**File:** `6-bonus.sql`  
Implements a stored procedure `AddBonus` that adds corrections for students.

### 7. Average score
**File:** `7-average_score.sql`  
Creates a stored procedure `ComputeAverageScoreForUser` that computes average scores.

### 8. Optimize simple search
**File:** `8-index_my_names.sql`  
Creates an index on the first letter of names.

### 9. Optimize search and score
**File:** `9-index_name_score.sql`  
Creates a composite index on name first letter and score.

### 10. Safe divide
**File:** `10-div.sql`  
Implements a function `SafeDiv` that handles division by zero.

### 11. No table for a meeting
**File:** `11-need_meeting.sql`  
Creates a view `need_meeting` for students needing meetings.

### 12. Average weighted score (Advanced)
**File:** `100-average_weighted_score.sql`  
Creates a procedure `ComputeAverageWeightedScoreForUser`.

### 13. Average weighted score for all! (Advanced)
**File:** `101-average_weighted_score.sql`  
Creates a procedure `ComputeAverageWeightedScoreForUsers` for all students.

## Requirements
- MySQL 5.7 on Ubuntu 18.04 LTS
- All SQL keywords in uppercase
- Files end with newline
- Descriptive comments before each task

## Setup
1. Start MySQL service:
   ```bash
   service mysql start
   ```
2. Execute SQL files:
   ```bash
   cat filename.sql | mysql -uroot -p database_name
   ```

## Resources
- MySQL cheatsheet
- Database indexing
- Stored procedures
- Triggers
- Views
- Functions and operators