# Data Model

### users
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| email | string | Unique (case-insensitive) |
| password_hash | string | Argon2id hash |
| role_id | int | Unique [1,2,3,4,5] |
| status | enum('active','disabled') | Account state |
| created_at | datetime | Default now() |

### roles
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| name | string | Unique (`guest`, `viewer`, `user`, `editor`, `admin`) |

### documents
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| title | string |  |
| content | text |  |
| created_by | fk(users.id) |  |
| created_at | datetime |  |
