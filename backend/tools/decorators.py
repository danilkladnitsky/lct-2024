def retry_on_exception(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception occurred: {e}. Retrying {retries + 1}/{max_retries}")
                    retries += 1
            raise Exception(f"Function {func.__name__} failed after {max_retries} retries")
        return wrapper
    return decorator
