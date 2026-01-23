import socket
from rich import print as rprint

def main_scan(port_min: int = 0, port_max: int = 1024, timeout: float = 0.1):
    host = '127.0.0.1'
    
    for i in range(port_min, port_max + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.settimeout(timeout)
            result = soc.connect_ex((host, i))

            protocol = 'неизвестен'
            try:
                protocol = socket.getservbyport(i, 'tcp')
            except (socket.error, OverflowError):
                pass

            if result == 0:
                rprint(f'порт {i:5} [#00FF66] ОТКРЫТ[/] (сервис: {protocol})')
            else:
                rprint(f'порт {i:5} [#FF6500] ЗАКРЫТ[/] (сервис: {protocol})')
def main_dns(guery: str = 'google.com'):
    try:
        ip = socket.gethostbyname(guery)
    except Exception as e:
        print(f'возникла ошибка {e}')
        ip = None

    rprint(f'запрос: [#00FF66] {guery}, [#00FFDD] ip-адрес: {ip}[/]')

if __name__ == '__main__':
    main_scan(0, 1000, 0.01)
    main_dns('python.org')
