def status(n):
    match n:
        case 200:
            return "OK BABY"
        case 404:
            return "NOT FOUND"
        case 500:
            return "Iternal server error"
        case _:
            return "Invalid error code"
            
print(status(200))
print(status(404))
print(status(500))
print(status(5000))
