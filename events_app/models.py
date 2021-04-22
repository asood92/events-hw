"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    events_attending = db.relationship(
        "Event", secondary="guest_events", back_populates="guests"
    )


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    guests = db.relationship(
        "Guest", secondary="guest_events", back_populates="events_attending"
    )


guest_event_table = db.Table(
    "guest_events",
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
)
