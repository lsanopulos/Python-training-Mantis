from model.project import Project
from random import randrange
from random import choice

def test_delete_some_group(app, db, config):
    username = config['web']['username']
    password = config['web']['password']
    old_projects = db.get_project_list()
    old_count = app.soap.count_projects(username, password)
    project = choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_count = app.soap.count_projects(username, password)
    assert old_count - 1 == new_count