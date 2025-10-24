# Authentication (AuthN)

Authentication verifies **who the user is** using email and password.

- Passwords are hashed with **Argon2id**.
- Access tokens are **JWT (HS256)** with 30-minute lifetime.
- JWT secret key defined as environment variable **`JWT_SECRET`**.

**JWT Claims**

sub → user ID
roles → list of roles
iat, exp → timestamps
