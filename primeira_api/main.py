from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float
    quantidade: int

app = FastAPI()

banco = []

@app.post("/item")
def add_item(novo_item:Item):
    banco.append(novo_item)
    return novo_item    

@app.get("/items/{id}")
def get_item(id: int):
    for item in banco:
        if id == item.id:
            return {
                "id": item.id,
                "descricao": item.descricao,
                "valor": item.valor,
                "quantidade": item.quantidade
            }

@app.get("/items")
def get_todos_items():
    return banco

@app.get("/items/valor_total")
def get_valor_total(): 
    valor_total = 0.0
    for item in banco:
        valor_total += item.valor * item.quantidade
    return valor_total

@app.delete("/item/{id}")
def delete_item(id: int):
    for item in banco:
        if id == item.id:
            banco.remove(item)
            print(banco)
            return banco




