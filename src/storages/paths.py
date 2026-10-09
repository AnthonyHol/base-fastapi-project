import platform


def get_updated_path_depending_on_os(path: str) -> str:
    if platform.system() == 'Windows':
        return path.replace('\\', '/')
    else:
        return path
