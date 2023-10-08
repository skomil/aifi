import uvicorn

def start():
    uvicorn.run('aifi.sample.greet:app', reload=True)

if __name__ == '__main__':
    start()