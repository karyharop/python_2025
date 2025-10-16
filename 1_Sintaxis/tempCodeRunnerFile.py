login("admin@gmail.com", "abcd1234") # False

login("admin@gmail.com", "1234") # True

login("usuario@gmail.com", "1234") # False

# Un ejemplo

if login("admin@gmail.com", "1234"):