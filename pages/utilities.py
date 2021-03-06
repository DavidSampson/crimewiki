file_type_dict = {
    'image': ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'raw', 'tiff', 'ai', 'svg'],
    'video': ['3gp', 'avi', 'flv', 'mp4', 'mkv', 'mpg', 'mpeg', 'm4v', 'mov', 'wmv', 'webm'],
    'pdf': ['pdf'],
    'audio': ['aiff', 'wav', 'flac', 'wma', 'mp3', 'aac', 'ogg', ]
}

file_types = tuple([(f, f)
                    for (f, v) in file_type_dict.items()]+[('other', 'other')])


def get_file_ending(name):
    return name.rpartition('.')[-1].lower()


def map_file_ending_to_type(ending):
    for k, v in file_type_dict.items():
        if ending in v:
            return k
    return 'other'


def map_file_to_type(name):
    return map_file_ending_to_type(get_file_ending(name))


def seqify(val):
    if not isinstance(val, (list, tuple)):
        return [val]
    else:
        return val


def one_of_these(*args):
    for arg in args[0:-1]:
        if arg:
            return arg
    raise args[-1]
