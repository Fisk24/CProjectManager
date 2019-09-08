import os

class ProjectParser():
    def __init__(self):
        self.rawProjectData = []

    def parseProject(self):
        # Return a dict containing project data values
        parsed = {}
        self._openFile(self._findProjectFile())
        for i in self.rawProjectData:
            key = i.split("=")[0]
            value = i.split("=")[1].strip("\n").strip("\"")
            parsed[key] = value

        return parsed

    def _findProjectFile(self):
        # Return the first project file that we happen across
        for i in os.listdir("."):
            if ".project" in i:
                return i

    def _openFile(self, fname):
        with open(fname, 'r') as raw:
            self.rawProjectData = raw.readlines()

if __name__ == "__main__":
    ProjectParser().parseProject()
