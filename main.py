from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
db = SQLAlchemy(app)

# здесь дофига всего пропущено

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    user = relationship("User", back_populates="projects")
    issue = relationship("Issue", back_populates="projects")


    def as_dict(self):
        return {'project_id': self.id, 'user_id': self.author_id, 'name': self.name}


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    projects = relationship("Project", back_populates="user")
    issue = relationship("Issues", back_populates="user")

    def as_dict(self):
        return {'id': self.id, 'name': self.name}

class Issue(db.Model):
    __tablename__ = 'issues'
    issue_id = db.Column(db.Integer, primary_key=True, autoincrement=True, )
    author_name = db.Column(db.String(255), ForeignKey('users.name'), nullable=False)
    assigned_name = db.Column(db.String(255), ForeignKey('users.name'), nullable=False)
    project_id = db.Column(db.Integer, ForeignKey('projects.project_id'), primary_key=True, autoincrement=True)
    issue_name = db.Column(db.String(255), nullable=False)

    user = relationship("User", back_populates="issue")
    projects = relationship("Project", back_populates="issue")

    def as_dict(self):
        return {'issue_id': self.issue_id, 'author_name': self.author_name, 'assigned_name': self.assigned_name,
                'project_id': self.project_id, 'issue_name:'}
