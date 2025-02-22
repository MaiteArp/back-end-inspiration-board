from app import db


class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship('Card', backref='board', lazy=True)


    def to_json(self):
        return {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner,
        }