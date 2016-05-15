from model.project import Project
import string
import random

def random_str(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app, config):
    name = random_str("ProjectName_", 10)
    desc = random_str("ProjectDescription", 10)
    username = config['web']['username']
    password = config['web']['password']
    old_count = app.soap.count_projects(username, password)
    app.project.create_project(name, desc)
    new_count = app.soap.count_projects(username, password)
    assert old_count + 1 == new_count