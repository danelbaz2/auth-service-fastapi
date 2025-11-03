from app.services.security import hash_password, verify_password

password = "Test13579!"

hashpass = hash_password(password)

print(hashpass)
print(len(hashpass))

input_password = "Test13579!"

try:
    verify_password(hashpass, input_password)
    print("Password verified successfully")
except:
    print("Password verification failed")

# python -m app.tests.hash_password