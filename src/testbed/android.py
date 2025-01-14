######################################################################
# Android App main loop
#
# The main loop itself is a no-op; however we need a PythonAppDelegate
# to satisfy the app stub.
#######################################################################
from rubicon.java import JavaClass, JavaInterface

# The Android cookiecutter template creates an app whose main Activity is
# called `MainActivity`. The activity assumes that we will store a reference
# to an implementation/subclass of `IPythonApp` in it.
MainActivity = JavaClass("org/beeware/android/MainActivity")

# The `IPythonApp` interface in Java allows Python code to
# run on Android activity lifecycle hooks such as `onCreate()`.
IPythonApp = JavaInterface("org/beeware/android/IPythonApp")


class PythonApp(IPythonApp):
    def __init__(self, app):
        super().__init__()
        self._impl = app
        MainActivity.setPythonApp(self)
        print("Python app launched & stored in Android Activity class")


def main_loop():
    pass
