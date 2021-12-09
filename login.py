from HDULogin.LoginManager import LoginManager

lm = LoginManager()
lm.login(
    username = input("Please input your account: "),
    password = input("Please input your password: ")
)
