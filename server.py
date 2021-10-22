from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import random
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('risk_free_rate')
parser.add_argument('beta_of_investment')
parser.add_argument('market_rise')


calculated_interests = {
    'cacluated1': {
        'risk_free_rate' : 3,
        'beta_of_investment': 1.3,
        'market_rise': 8,
        'result': 9
    }
}


# create route for calculator
@app.route('/')
def index():
    return render_template('index.html')


class Calculate(Resource):
    def get(self):
        return calculated_interests
    def post(self):
        args = parser.parse_args()
        # calculated_id =int(max(calculated_interests.keys()).lstrip('calculate')) + 1
        calculated_id = random.randint(0, 22)
        calculated_id = 'calculated%i' %calculated_id
        print(args)
        risk_free_rate = int(args['risk_free_rate'])
        beta_of_investment = int(args['beta_of_investment'])
        market_rise = int(args['market_rise'])
        result = (risk_free_rate / 100) + beta_of_investment * (( market_rise /100) + (risk_free_rate / 100))
        print(result)
        calculated_interests[calculated_id] = {
            'risk_free_rate': risk_free_rate,
            'beta_of_investment': beta_of_investment,
            'market_rise': market_rise,
            'result': result
        }
        return calculated_interests[calculated_id]

api.add_resource(Calculate, '/calculate')

if __name__ == '__main__':
    app.run()
