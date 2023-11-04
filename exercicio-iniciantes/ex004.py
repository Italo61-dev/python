
def new_func():
    meters = float(input('Uma distância em metros: '))
    km = meters / 1000
    hm = meters / 100
    dam = meters / 10
    dm = meters / 0.1
    cm = meters / 0.01
    mm = meters / 0.001
    print('A media de {}\n{} km\n{} hm\n{} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm'.format(meters, km, hm, dam, dm, cm, mm))

new_func()