def login(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    password = "admin1234"
    result = db.execute(query)
    return result

def get_data(items):
    for i in range(len(items)):
        for j in range(len(items)):
            print(items[i], items[j])
