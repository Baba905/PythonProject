class User:
    def __init__(self, name):
        self.name =name
        self.is_connected = False


def is_authentificated_decorator(function):
    def wrappeer(*args, **kwargs):
        if args[0].is_connected:
            function(args[0])
    return wrappeer

@is_authentificated_decorator
def create_a_blog_post(user):
    print(f"This is  {user.name} new post.")

new_user =User('Baba')
new_user.is_connected =True
create_a_blog_post(new_user)