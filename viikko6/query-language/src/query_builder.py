from matchers import All, HasFewerThan, PlaysIn, HasAtLeast, And, Or
class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher
    def build(self):
        return self._matcher
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1,query2))