def get_from_dict(dictionary: dict, key: str, default_value=""):
    """Wrapper to get a dictionary value

    Args:
        dictionary (dict): Data Dictionary
        key (str):
        default_value (str, optional): Default value in case there is no coincidence

    Returns:
        Any: value
    """
    value = dictionary.get(key)

    if value is None:
        return default_value
    return value
