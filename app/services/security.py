from argon2 import PasswordHasher, exceptions as argon2_exc

# Default parameters
PH = PasswordHasher(
    time_cost=3,        # number of iterations
    memory_cost=64_000,
    parallelism=2,
    hash_len=32,
)

def hash_password(password: str) -> str:
    return PH.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    try:
        PH.verify(hashed, plain)
        return True
    except argon2_exc.VerifyMismatchError:
        return False
    except argon2_exc.InvalidHash:
        return False

def needs_rehash(hashed: str) -> bool:
    try:
        return PH.check_needs_rehash(hashed)
    except argon2_exc.InvalidHash:
        return True
