from datetime import datetime

from flask_login import login_required, current_user
from flask_restful import Resource

from app import accuweather
from app.models import SearchHistory
from app.config import db
from app.hardcodedata import WeatherMessages, api_key


class GetWeather(Resource):
    @login_required
    def get(self, location):
        city = location.title()

        city_code = accuweather.get_code(city, api_key)
        if not city_code:
            return {'message': WeatherMessages.change_key}

        weather_data = accuweather.get_weather(city_code, api_key)
        tempf = weather_data["Temperature"]["Imperial"]["Value"]
        tempc = weather_data["Temperature"]["Metric"]["Value"]
        now_t = datetime.now()
        now_s = now_t.strftime("%d-%m-%Y, %H:%M:%S")
        show = {
            'city': city,
            'tempf': tempf,
            'tempc': tempc
        }

        locs = SearchHistory(location=city, temp_in_c=tempc, temp_in_f=tempf, times=now_s, user_id=current_user.id)
        db.session.add(locs)
        db.session.commit()
        return {'weather data': show}