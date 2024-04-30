first_name_schema = {
    "type": "string",
    "minlength": 3,
    "maxlength": 30,
    "required": True,
    "empty": False,
}

last_name_schema = {
    "type": "string",
    "minlength": 3,
    "maxlength": 30,
    "required": True,
    "empty": False,
}

email_schema = {
    "type": "string",
    "minlength": 3,
    "maxlength": 200,
    "required": True,
    "empty": False,
    "regex": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
}
