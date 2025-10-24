# Register Flow

**Type:** Auto-activation (no admin approval)

### Steps
1. Receive `{email, password}`
2. Validate (email format, password ≥ 8 chars)
3. Normalize email (trim + lower)
4. Check for duplicates (case-insensitive)
5. Hash password with Argon2id
6. Create user with status `active` and role `guest`
7. Return `201 Created` with `{id, email, created_at, roles: ['guest']}`

### Rate Limit
- 5 requests / 5 minutes per IP

### Errors
| Case | Code |
|------|------|
| Invalid data | 422 |
| Email exists | 409 |
| Server error | 500 |

