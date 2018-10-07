from flask import Flask

app = Flask(__name__)

import code.routing
import code.login
import code.signup
