import time


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        execution_time = end_time - start_time
        log_data = f"Path: {request.path}, Method: {request.method}, Execution Time: {execution_time:.2f} seconds\n"
        with open(
            "log.txt", "a"
        ) as file:
            file.write(log_data)
        return response
