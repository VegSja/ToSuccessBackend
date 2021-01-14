from .models import Stats

import json

def main():
    test_data = {
        "Hello":"World"
    }

    json_test = json.dumps(test_data)

    data_test = Stats(data=json_test, username="TestUsername")
    data_test.save()

    objects = Stats.objects.all()
    print(objects)
    return

main()

