class MatchManagerRouter:
    route_app_labels = {"matches"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "matches"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "matches"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {obj1._state.db, obj2._state.db}
        if len(db_set) == 1:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "matches"
        return db == "default"