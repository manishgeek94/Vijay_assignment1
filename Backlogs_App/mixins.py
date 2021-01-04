from django.core.serializers import serialize
import json


class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            stud_data = obj['fields']
            final_list.append(stud_data)
        json_data = json.dumps(final_list)
        return json_data

# we are doing this adding to empty list and then to again to json because serialize function some extra meta data - which we don't need in our code
# and we need fields
