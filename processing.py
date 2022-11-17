def do_calculation(number1, number2):
    return number1 + number2

def cake_flour(g_cake):
    ratio_apf = 105./120
    ratio_corn = 14./120

    g_apf = g_cake * ratio_apf
    g_corn = g_cake * ratio_corn

    return  '{} grams cake flour =<br> {}g APF + {}g cornstarch'.format(g_cake, g_apf, g_corn)