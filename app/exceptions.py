class SurveyNotFoundException(Exception):
    def __init__(self, id):
        super().__init__("Survey with id: " + str(id) + " does not exist")