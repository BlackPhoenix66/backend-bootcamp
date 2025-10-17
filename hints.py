users = {
    101: {'name': 'Denis', 'email': 'apertn@nt.com', 'active': True},
    102: {'name': 'End', 'email': 'rerere@mag.com', 'active': False},
    103: {'name': 'Kekw', 'email': 'laugh@nrj.com', 'active': True}
}
users[102]['active'] = True
users[104] = {'name':'Fiel', 'email': 'reap@maiel.com', 'active': True}
deleted_users = users.pop(101)
print(deleted_users)
print(users[102]['active'])
print(users[103]['email'])
print(users[104])
print(users[102]['active'])