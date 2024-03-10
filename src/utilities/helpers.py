import uuid


def _generate_filename(instance, filename):
    *_, ext = filename.split('.')
    name = uuid.uuid4().hex
    filename = f'{name}.{ext}'
    return filename

def farm_photos_path(instance, filename):
    filename = _generate_filename(instance, filename)
    return f'farm/photos/{filename}'

def farm_crop_photos_path(instance, filename):
    filename = _generate_filename(instance, filename)
    return f'farm/crops/photos/{filename}'