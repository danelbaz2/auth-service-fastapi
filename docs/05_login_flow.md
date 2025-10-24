# Login Flow

### Steps
1. Receive `{email, password}`
2. Normalize email
3. Find user (must be active)
4. Verify password with Argon2id
5. Generate JWT (HS256, TTL 30m)
6. Return `{access_token, token_type: "bearer"}`

### Rate Limit
- 5 requests / 5 minutes per IP

### Errors
| Case | Code |
|------|------|
| Invalid credentials | 401 |
| Inactive account | 403 |
| Too many attempts | 429 |

