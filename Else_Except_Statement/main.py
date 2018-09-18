import json

for i in range():
    print("")
else:
    print("done !")


def divide_json(path):
    handle = open(path, "r+")
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
            op["numerator"] /
            op["denominator"]
        )
    except ZeroDivisionError as e:
        return None
    else:
        op["result"] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()
