from ray import serve
import starlette

@serve.deployment
def hello_world(request: starlette.requests.Request):
    return f"Hello, {request.query_params.get('name', 'Ray')}!"

app = hello_world.bind()
