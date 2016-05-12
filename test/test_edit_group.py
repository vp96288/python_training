# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="New group")
    group.id = random_group.id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="new_header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)