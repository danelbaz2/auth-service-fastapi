# Logging Policy

Structured logs (JSON preferred).

**Levels**
- DEBUG — internal details
- INFO — success events (login, register)
- WARNING — invalid attempts, rate limits
- ERROR — unexpected server errors
- CRITICAL — unrecoverable failures

**Never log:**
- Plain passwords
- JWTs or sensitive tokens

Each log includes:
`timestamp, level, event, request_id, ip, user_id (if auth), outcome`
