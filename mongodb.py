from flask_pymongo import PyMongo

class MyMongo(PyMongo):

    def save_to_db(self, data):
        self.db.users.insert_one(data)
        return {
            'username' : data['username'],
            'password': data['password'],
            'email': data['email']
            }
    
    def find_one_by_name(self, name):
        users = self.db.users.find_one({'username': name})
        return {
            'username' : users['username'],
            'password': users['password'],
            'email': users['email']
        }

    def find_all_by_name(self, name):
        users = self.db.users.find({'username': name})
        # result = [user.pop('_id') for user in users]
        result = [user for user in users if user.pop('_id')]

        # for user in users:
        #     user.pop('_id')
        #     result.append(user)

        return result

    def find_all(self):
        users = self.db.users.find()
        result = {}
        index = 1
        for user in users: 
            user.pop('_id')
            result[index] = user
            index += 1

        return result
