from __main__ import app

@app.route('/smh', methods=['GET'])
def test():
    return 'it works!'