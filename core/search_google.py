from googlesearch import search

def search(query: str, number: int) -> list:
    res = search(query, num_results=number, unique=True)
    return res


if __name__ == "__main__": 
    query = "virtual idol"
    res = search(query, 5)
    print(res)