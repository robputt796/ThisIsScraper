from flask import Flask
from flask import g
from flask import render_template
from this_is_scraper.db import get_db_session
from this_is_scraper.db import Articles


app = Flask(__name__)


@app.before_request
def pre_req():
    g.db = get_db_session()    


@app.after_request
def post_req(resp):
    try:
        g.db.close()
    except:
        pass
    return resp


def get_articles():
    articles = g.db.query(Articles).order_by(Articles.article_dt.desc()).all()
    return articles


@app.route('/')
def display_article_list():
    articles = get_articles()
    return render_template('article_list.html',
                           articles=articles)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, threaded=True, debug=True)
