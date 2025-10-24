# Data Model

### users
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| email | string | Unique (case-insensitive) |
| password_hash | string | Argon2id hash |
| status | enum('active','disabled') | Account state |
| created_at | datetime | Default now() |

### roles
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| name | string | Unique (`guest`, `viewer`, `user`, `editor`, `admin`) |

### user_roles
| Column | Type | Description |
|---------|------|-------------|
| user_id | fk(users.id) |  |
| role_id | fk(roles.id) |  |
| unique(user_id, role_id) |  | prevent duplicates |

### documents
| Column | Type | Description |
|---------|------|-------------|
| id | int | Primary key |
| title | string |  |
| content | text |  |
| created_by | fk(users.id) |  |
| created_at | datetime |  |
