import redis

r = redis.Redis(host='127.0.0.1', port=6379)

r.mset({'Croatia': 'Zagreb', 'Bahamas': 'Nassau'})

print(r.get('Croatia').decode('utf-8'))

r.lpush