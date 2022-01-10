from HDULogin.LoginManager import LoginManager
from getpass import getpass
hdu = LoginManager()
hdu.login(
    username = input("Please input your account: "),
    password = getpass("Please input your password: ")
)
