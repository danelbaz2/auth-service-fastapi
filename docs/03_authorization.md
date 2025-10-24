# Authorization (AuthZ)

Authorization defines **what a user can do**, based on their role.

## Roles hierarchy

guest < viewer < user < editor < admin

## Access Matrix

| Route | Min Role |
|-------|-----------|
| GET /users/me | guest |
| GET /users | admin |
| POST /users/{id}/roles | admin |
| GET /documents/{doc_id} | viewer |
| POST /documents | user |
| PATCH /documents/{doc_id} | user |
| DELETE /documents/{doc_id} | editor |

Public routes: `/health`, `/auth/register`, `/auth/login`

