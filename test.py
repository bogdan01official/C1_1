from main import PortScan


def main():
    target = input('\n[*] Введите доме или IP-адрес для сканирования')
    port_count = int(input('[*] Введите количество портов для сканирования (1000 по умолчанию)') or 1000)
    print('\n- Сканирую...', end='')
    scan = PortScan(target, port_count)
    scan.port_rotate()
    print('\r- Выполнено', end='')

    banners = scan.banners_port
    o_port = scan.open_port

    if len(banners) == 0 and len(o_port) == 0:
        print('открытых портов не найдено.')
        return
    else:
        if target.startswith('http'):
            target_print = target.split("/")[2]
            print(f"\n\nСВОБОДНАЯ ИНФОРМАЦИЯ ПО ДОМЕНУ (IP): {target_print}\n{'*' * 50}")
        else:
            print(f"\n\nСВОБОДНАЯ ИНФОРМАЦИЯ ПО ДОМЕНУ (IP): {target}\n{'*' * 50}")
        for bann in banners:
            print(f'  Порт {bann:5}  Баннер: {banners[bann]}')
        for o in o_port:
            print(f'   Порт: {o:5}  Сервис: {o_port[o]}')

if __name__ == "__main__":
    main()