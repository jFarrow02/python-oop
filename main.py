from user import User
from post import Post

user_1 = User("foo@bar.com", 'Foo Jenkins', "foo22", "DevOps Engineer")
user_1.get_user_info()

post_1 = Post("This is a new post", user_1.name)

post_1.get_post_info()

