from biothings.web.launcher import FlaskAPILauncher

application = FlaskAPILauncher("config").get_server()
