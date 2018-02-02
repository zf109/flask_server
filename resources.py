"""
    Resource file for machine learning application
"""
from flask_restful import Resource
from flask import request
import ast
from processes import simple_process


class SimpleResource(Resource):
    """
        Sets model parameters
    """
    def get(self):
        """
            Get method obtains model
        """
        return "Now you get me!"

    def put(self):
        """
            Put method sets model prarameters (MODEL_PARAMETERS),
            the format should be MODEL_PARAMETERS[<model_name>][<param_name>]
            as a json file.
        """
        data = ast.literal_eval(request.form['data'])
        return simple_process(data), 200

