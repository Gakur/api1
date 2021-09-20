from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("email", type=str, required=True, help="Please input an email")
parser.add_argument("username", type=str, required=True, help="Please input your username")
parser.add_argument("work_time", type=int, required=True, help="Please input working time")
parser.add_argument("break_time", type=str, required=True, help="Please input time taken for a break")
parser.add_argument("break_task", type=str, required=True, help="Please input what you will be doing at break time")




class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        email = args["email"]
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]
        work_time = args["work_time"]
        break_time = args["break_time"]
        break_task = ["break_task"]


        newUser = UserModels(username, email, password, confirm_password,  work_time, break_time, break_task )
        newUser.save_user()

        return {
            "message": "Work begins now..Remember to take a break",
            "user" : newUser.__dict__
        }, 201

    def get(self):
        pass