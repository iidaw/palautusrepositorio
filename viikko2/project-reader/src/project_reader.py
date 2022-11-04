from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)


        new_content = toml.loads(content)

        info = new_content["tool"]["poetry"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
        return Project(info["name"], info["description"], info["dependencies"], info["dev-dependencies"])



#print(toml.load("pyproject.toml"))
