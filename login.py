from HDULogin.LoginManager import LoginManager

hdu = LoginManager()
hdu.login(
    username = input("Please input your account: "),
    password = input("Please input your password: ")
)
