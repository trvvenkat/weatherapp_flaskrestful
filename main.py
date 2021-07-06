from app import views
from app.config import api, app

# api.add_resource(views.Index, '/check')
api.add_resource(views.Signup, '/signup')
api.add_resource(views.Login, '/login')
api.add_resource(views.GetWeather, '/weather/<location>')
api.add_resource(views.Logout, '/logout')

if __name__ == '__main__':
    app.run(debug=True)
