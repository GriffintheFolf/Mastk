# entry point for Mastk

from Application import Application

if __name__ == "__main__":
    from LoginScreen import LoginScreen

    app = Application("Mastk")
    LoginScreen(app)
    app.mainloop()
