import socket
from rich import print

def main(port_min: int = 0, port_max: int = 1024, ожидание: float = 0.1):
    host = '127.0.0.1'
    
    for i in range(port_min, port_max + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.settimeout(ожидание)
            result = soc.connect_ex((host, i))

            protocol = 'неизвестен'
            try:
                protocol = socket.getservbyport(i, 'tcp')
            except (socket.error, OverflowError):
                pass

            if result == 0:
                print(f'порт {i:5} [#00FF66] ОТКРЫТ[/] (сервис: {protocol})')
            else:
                print(f'порт {i:5} [#FF6500] ЗАКРЫТ[/] (сервис: {protocol})')

if __name__ == '__main__':
    main()
