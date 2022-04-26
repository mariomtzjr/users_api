import os

from flask import Blueprint, render_template, request, current_app

from sqlalchemy.orm import Session, Query

from flask_paginate import Pagination, get_page_args

from app.main.models import User
from app.main.database import db

users_blueprint = Blueprint('users_blueprint', __name__, template_folder='templates', static_folder='static')

@users_blueprint.route('/users/', methods=['GET'])
@users_blueprint.route('/')
def index():
    params = request.args
    print("params: ", params)
    
    session = Session(db)

    users = Query([User], session=session)
    total = users.count()
    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="pp", pp=5
    )

    pagination = Pagination(
        page=page,
        total=total,
        pp=per_page,
        format_total=True,
        format_number=True,
        page_parameter="page",
        per_page_parameter="pp",
        record_name='users', css_framework='bootstrap4')

    return render_template('user_list.html', users=users, pagination=pagination)


@users_blueprint.route("/users", defaults={"page": 1})
@users_blueprint.route("/users/page/<int:page>")
def users(page):
    session = Session(db)

    users = Query([User], session=session)
    total = users.count()

    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="pp", pp=5
    )

    pagination = get_pagination(
        page=page,
        per_page=per_page,
        total=total,
        record_name="users",
        format_total=True,
        format_number=True,
    )
    return render_template('user_list.html', users=users, pagination=pagination, active_url="users-page-url")




def get_pagination(**kwargs):
    kwargs.setdefault("record_name", "users")
    return Pagination(
        css_framework="bootstrap4",
        **kwargs
    )