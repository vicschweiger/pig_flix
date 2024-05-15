from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///filmes.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


app = Flask(__name__)

class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(40), index=True)
    url = Column(String)
    cover_img = Column(String)
    launch_date = Column(String)
    
    def __repr__(self):
        return '<Movie {}>'.format(self.title)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_movie')
def add_movie():
    return render_template('add_movie.html')

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':

        title = request.form['title']
        url = request.form['url']
        cover_img = request.form['cover_img']
        launch_date = request.form['launch_date']
        
        new_movie = Movies(title=title, url=url, cover_img=cover_img, launch_date=launch_date)
        
        db_session.add(new_movie)
        db_session.commit()
        
        return render_template('add_movie.html')

if __name__ == "__main__":
    app.run(debug=True)