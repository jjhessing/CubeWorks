import serial
import asyncio

async def readSerial():
	serialport = serial.Serial('/dev/serial0', 115200)
	while True:
		if serialport.in_waiting:
			data = serialport.read_until(b'\r')
			print(data.decode('utf-8'))
			await asyncio.sleep(1)
		else:
			print('buffer empty')
			await asyncio.sleep(1)

async def otherFunction():
	while True:
		print('Other functionalities running')
		await asyncio.sleep(1)

async def main():
	asyncio.create_task(readSerial())
	#asyncio.create_task(otherFunction())
	while True:
		#print('even more functionality')
		await asyncio.sleep(2)

if __name__ == '__main__':
	asyncio.run(main())
