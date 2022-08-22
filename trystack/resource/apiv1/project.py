from flask_restful import Resource

from trystack.controller.apiv1 import ProjectController


class ProjectResource(Resource):
    def get(self, project_id=None):
        """
        GET /projects --> Project list
        GET /projects/<project_id> --> Project info
        """
        if project_id is None:
            return ProjectController.get_projects()
        else:
            return ProjectController.get_project(project_id)

    def post(self):
        """
        POST /projects --> Create a new project
        POST /projects/<project_id> --> Not allowed
        """
        return ProjectController.create_project()

    def patch(self, project_id):
        """
        PATCH /projects --> Not allowed
        PATCH /projects/<project_id> --> Update project
        """
        return ProjectController.update_project(project_id)

    def delete(self, project_id):
        """
        DELETE /projects --> Not allowed
        DELETE /projects/<project_id> --> Delete project
        """
        return ProjectController.delete_project(project_id)
