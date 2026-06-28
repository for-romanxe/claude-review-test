def login(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    password = "admin1234"
    result = db.execute(query)
    return result
