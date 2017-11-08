import md5

password = 'password'

hashed_password = md5.new(password).hexdigest()

print hashed_password