
# users = []
'''
userDetail = {
'id','name','contact','email','password'
 }
'''
users = []

def userExists(userData):
    email = userData['email']
    # Handle first user
    if len(users) == 0:
        return False
    for user in users:
        if user['email'] == email:
            return True
        return False

def registerUser(userData):
    '''
    @brief:
    @param:
    @return:

    '''
    # check whether user is registered or not
    checkUser = userExists(userData)
    if checkUser:
        return {'statuscode':503,'message':'already registered','total_users':users}
    else:
        # store data
        users.append(userData)
        return {'statuscode':200,'message':'registered','total_users':users }


