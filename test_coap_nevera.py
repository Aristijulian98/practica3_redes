import logging
import asyncio
import random
from time import sleep

from aiocoap import *

# put your service name here
ESP32_MDNS = "my_nevera_control_app.local"

# define the URIs and PAYLOADs
URITEMP = "nevera/temp"

URIALRMA = "nevera/alarma"

URILIQUIDO = "nevera/liquido"
    
URIENERGIA = "nevera/energia"
energia = b"SI"

URIBLOQUEO = "nevera/bloqueo"
PAYLOADBLOQUEO = b" NO"

URITIEMPO = "nevera/tiempo"
PAYLOADTIEMPO = b"0 mins"

logging.basicConfig(level=logging.INFO)

async def get(ip, uri):
    protocol = await Context.create_client_context()
    request = Message(code = GET, uri = 'coap://' + ip + '/' +  uri)
    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %r'%(response.payload))
        global energia
        energia = response.payload

async def put(ip, uri, payload):
    context = await Context.create_client_context()
    await asyncio.sleep(2)
    request = Message(code = PUT, payload = payload, uri = 'coap://' + ip +'/' + uri)
    response = await context.request(request).response
    #print('Result: %r'%(response.payload))

async def delete(ip, uri):
    context = await Context.create_client_context()
    await asyncio.sleep(2)
    request = Message(code = DELETE, uri = 'coap://' + ip +'/' + uri)
    response = await context.request(request).response
    print('Result: %r'%(response.payload))

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    for i in range(10):
        flagt = 0
    
        print("*** START DATA LECTURE ***")
        print("*** TEMPERATURA DENTRO DE LA NEVERA: ***")
        asyncio.run(get(ESP32_MDNS, URITEMP))
        sleep(3)
        
        print("*** ALARMA DE TEMPERATURA ACTIVADA? ***")
        asyncio.run(get(ESP32_MDNS, URIALRMA))
        sleep(3)
        
        print("*** DETECCION DE DERRAME DE LIQUIDO? ***")
        asyncio.run(get(ESP32_MDNS, URILIQUIDO))
        sleep(3)
        
        print("*** ENERGIA CONSTANTE EN EL DISPOSITIVO? ***")
        asyncio.run(get(ESP32_MDNS, URIENERGIA))
        
        if energia == b'NO':
            PAYLOADBLOQUEO = b" SI"
            flagt = 1
        else:
            PAYLOADBLOQUEO = b" NO"
        
        #print("*** PUT BLOQUEO ***")
        asyncio.run(put(ESP32_MDNS, URIBLOQUEO, PAYLOADBLOQUEO))
        print("*** BLOQUEO DE PUERTAS ACTIVO? ***")
        asyncio.run(get(ESP32_MDNS, URIBLOQUEO))
        
        if flagt == 1:
            time = random.randint(1,9)
            tiempo = str(time)
            t = tiempo.encode()
            PAYLOADTIEMPO = t + b" mins"
        else:
            PAYLOADTIEMPO = b"0 mins"
        
        #print("*** PUT TIEMPO  ***")
        asyncio.run(put(ESP32_MDNS, URITIEMPO, PAYLOADTIEMPO))
        print("*** TIEMPO DE BLOQUEO: ***")
        asyncio.run(get(ESP32_MDNS, URITIEMPO))
                 
        sleep(5)
        