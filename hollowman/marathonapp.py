

from marathon.models.app import MarathonApp


class SieveMarathonApp(MarathonApp):

    def get_constraints_by_name(self, consraint_name):
        result = []
        for c in self.constraints:
            if c.field == consraint_name:
                result.append(c)
        return result

    def remove_constraints_by_name(self, consraint_name):
        result = []
        for c in self.constraints:
            if c.field != consraint_name:
                result.append(c)
        self.constraints = result

    def has_constraint(self, name):
        return len(self.get_constraints_by_name(name))

