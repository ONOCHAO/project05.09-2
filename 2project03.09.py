import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:5001"
    async with websockets.connect(uri) as websocket:
        # Запуск автообновления
        await websocket.send(json.dumps(["start"]))
        response = await websocket.recv()
        print("Ответ:", json.loads(response))

        # Получение нескольких курсов
        for _ in range(3):
            msg = await websocket.recv()
            print("Курс:", json.loads(msg))

        # Остановка
        await websocket.send(json.dumps(["stop"]))
        stop_response = await websocket.recv()
        print("Ответ:", json.loads(stop_response))

asyncio.run(test())
