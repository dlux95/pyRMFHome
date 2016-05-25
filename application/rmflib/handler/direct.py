from application import app
from application.decorators import crossdomain
from application.rmflib.remotes import remote


@app.route('/api/v1.0/direct_press/<string:buttonkey>', methods=['GET'])
@crossdomain(origin='*', headers="Content-Type,Accept")
def direct_press(buttonkey):
    mapping = {
        "BACK_LEFT"     : remote.pressBackLeft,
        "BACK_HIGH"     : remote.pressBackHigh,
        "BACK_LOW"      : remote.pressBackLow,
        "FRONT_LEFT"    : remote.pressFrontLeft,
        "FRONT_RIGHT"   : remote.pressFrontRight,
        "FRONT_UP"      : remote.pressFrontUp,
        "FRONT_DOWN"    : remote.pressFrontDown,
        "FRONT_CENTER"  : remote.pressFrontCenter
    }
    if mapping.has_key(buttonkey):
        mapping[buttonkey]()
        return "{'error': 'OK'}"
    else:
        return "{'error': 'NO_SUCH_KEY'}"
