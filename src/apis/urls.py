from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login", views.login, ["POST"], "Login API"),
    ("/users/register", views.register_user, ["POST"], "Create user API"),
]

other_urls = []

all_urls = api_urls + other_urls
