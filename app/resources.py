from flask import Blueprint, render_template, request, jsonify, abort

from sqlalchemy.orm import Session, Query
from sqlalchemy import create_engine, asc, desc

from flask_paginate import Pagination, get_page_args

from app.main.models import User
from app.main.schemas import UserSchema
from scripts.seed import get_database_path

users_blueprint = Blueprint(
    'users_blueprint',
    __name__,
    template_folder='templates',
    static_folder='static'
)
profile_blueprint = Blueprint('profile_blueprint', __name__)

db = create_engine(f"sqlite:////{get_database_path('github_users.db')}")
session = Session(db)

@users_blueprint.route('/users/', methods=['GET'])
@users_blueprint.route('/')
def index():
    params = request.args
    print("params: ", params)
    
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


@profile_blueprint.route('/users/profiles/', methods=['GET'])
def list_profile():

    persons = Query([User], session=session)
    user_schema = UserSchema(many=True)

    data = user_schema.dump(persons)
    
    start = request.args.get('start', 1)
    pagination = request.args.get('pagination', 25)
    page = request.args.get('page', 1)
    order_by = request.args.get('order_by', 'id')
    username = request.args.get('username', None)
    id = request.args.get('id', None)

    if order_by == "id":
        filtered_data = Query([User], session=session).order_by(desc(order_by))
        data = user_schema.dump(filtered_data)
    elif order_by == "type":
        filtered_data = Query([User], session=session).order_by(asc(order_by))
        data = user_schema.dump(filtered_data)
    
    if username:
        filtered_data = Query([User], session=session).filter(User.username == username)
        data = user_schema.dump(filtered_data)
    
    if id:
        filtered_data = Query([User], session=session).filter(User.id == int(id))
        data = user_schema.dump(filtered_data)
    
    return jsonify(get_paginated_list(data, 
        '/users/profiles/',
        page=page,
        id=id,
        username=username,
        start=start, 
        pagination=pagination
    ))
    

def get_paginated_list(results, url, page, id, username, start, pagination):
    page = int(page)
    start = int(start)
    pagination = int(pagination)
    count = len(results)
    
    if count < start or pagination < 0:
        abort(404)
    
    # make response
    if id or username:
        response = results
        return response

    obj = {}
    obj['page'] = page
    obj['start'] = start
    obj['pagination'] = pagination
    obj['count'] = count
    
    items_per_page = count // pagination
    items_per_page_remainder = count % pagination

    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        page = page - 1 if page > 1 else 1
        start_copy = max(1, start - pagination)
        limit_copy = pagination
        obj['previous'] = url + '?page=%d&start=%d&pagination=%d' % (page, start_copy, limit_copy)
    
    # make next url
    if start + pagination > count:
        obj['next'] = ''
    else:
        start_copy = start + pagination
        next_page = page + 1

        obj['next'] = url + '?page=%d&start=%d&pagination=%d' % (next_page, start_copy, pagination)

    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + pagination)]
    return obj


def get_pagination(**kwargs):
    kwargs.setdefault("record_name", "users")
    return Pagination(
        css_framework="bootstrap4",
        **kwargs
    )