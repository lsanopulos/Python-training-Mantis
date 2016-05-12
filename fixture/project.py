from model.project import Project
import string
import random

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        '''if wd.find_element_by_css_selector("td.form-title").text == 'APPLICATION ERROR #701':
            self.open_projects_page()
            wd.find_element_by_css_selector('input[value="Create New Project"]').click()
            self.fill_new_project_form(project)'''

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def fill_new_project_form(self, project):
        wd = self.app.wd
        symbol = string.ascii_letters + string.digits
        self.change_field_value("name", project.name + str(random.choice(symbol)))
        self.change_field_value("description", project.description + str(random.choice(symbol)))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Proceed").click()

    def open_projects_page(self):
        # open projects page
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_element_by_css_selector('input[value="Create New Project"]')) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(id)
        #submit deletion
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        #confirmation
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_edit_page.php?project_id=%s" % id)
        #wd.find_element_by_css_selector("input[value = '%s']" % id).click()







