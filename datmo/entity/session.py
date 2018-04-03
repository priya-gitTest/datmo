from datetime import datetime

class Session():
    def __init__(self, dictionary):
        self.id = dictionary['id']
        self.name = dictionary['name']
        self.model_id = dictionary['model_id']

        self.created_at = dictionary.get('created_at', datetime.utcnow())
        self.updated_at = dictionary.get('updated_at', self.created_at)

    def __eq__(self, other):
        return self.id == other.id if other else False

    def toDictionary(self):
        attr_dict = self.__dict__
        pruned_attr_dict = { attr: val
                    for attr, val in attr_dict.iteritems() if not callable(getattr(self, attr)) and not attr.startswith("__")
        }
        return pruned_attr_dict