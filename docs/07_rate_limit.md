# Rate Limiting

Applied to `/auth/register` and `/auth/login`.

- **Limit:** 5 requests / 5 minutes / IP
- **Response:** 429 Too Many Requests
- **Purpose:** Prevent brute-force and spam signups.
