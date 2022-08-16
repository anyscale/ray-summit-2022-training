import aiohttp
import tqdm
import time
import asyncio

SERVE_URL = "http://localhost:8000"


async def async_http_get(path: str, session, pbar):
    """Send an HTTP request with asyncio"""
    async with session.get(SERVE_URL + path) as response:
        result = await response.text()
        pbar.update(1)
        return result
    
async def load_test(path: str, num_requests=10):
    """ Send  parallel requests to the endpoint """
    with tqdm.tqdm(total=num_requests, desc='Running load test') as pbar:
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            reqs = [async_http_get(path, session, pbar) for i in range(num_requests)]
            results = await asyncio.gather(*reqs)
            total_time = time.time() - start_time

    qps = round(num_requests/total_time, 3)
    avg_time = round(total_time / num_requests, 3)
    
    print(f"Sent {num_requests} requests in {total_time}. {qps} QPS average. {avg_time}s per request.")
    return qps

def inefficient_fib(n=None):
    """Compute intensive calculation for the nth fibonacci number"""
    if n <= 1:
        return n
    return inefficient_fib(n - 1) + inefficient_fib(n - 2)

def compute_intensive_workload():
    r = inefficient_fib(33)
    return f"The 33nd fibonacci number is {r}"

class ComputeIntensiveModel:
    def forward(self):
        return compute_intensive_workload()