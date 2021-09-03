from app import db
from datetime import datetime


class Test(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    release_year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def __repr__(self) :
        return f"{self.title} ({self.release_year})"

class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(50))
    comments = db.relationship("Comment", backref="writer", lazy=True)

    def __repr__(self) :
        return f"Users: {self.name}"
    
class Comment(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", onupdate="CASCADE"), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    posted_on = db.Column(db.Integer, nullable=False) # 댓글 달린 게시글 번호

    def __repr__(self) :
        return f"Comments: posted on {self.posted_on}({self.created_date})"