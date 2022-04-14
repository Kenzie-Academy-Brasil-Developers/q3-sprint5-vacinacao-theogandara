from datetime import datetime

def data_generate():
        now = datetime.now()
        return now.strftime("%a, %d %b %Y %H:%M GMT")