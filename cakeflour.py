import argparse

#1 cup cakeflour = 1 cup APF - 2 tbsp APF + 2 tbsp cornstarch
#(based off KAF) assuming 1 cup APF = 120g, 1/4 cup cornstarch = 28g
#https://www.kingarthurbaking.com/learn/ingredient-weight-chart

ratio_apf = 105./120
ratio_corn = 14./120

def parse_cmdline(): 
    parser = argparse.ArgumentParser(description='Convert cakeflour to APF and cornstarch mixture')
    #parser.add_argument('-g', '--grams', type=int, help='grams of cake flour needed', required='true')

    meas = parser.add_mutually_exclusive_group(required=True)
    meas.add_argument('-g', '--grams', type=int, help='grams of cake flour needed')
    meas.add_argument('-c', '--cups', type=float, help='cups of cake flour needed')

    args = parser.parse_args()


    if args.cups:
        #1 cup cake flour = 120g
        g = args.cups * 120
        print(args.cups, "cups cakeflour =", g, "grams cakeflour")
    else: g = args.grams

    return [g]


def main():
    #print("Hello World!")
    [g_cake] = parse_cmdline()

    g_apf = g_cake * ratio_apf
    g_corn = g_cake * ratio_corn

    print(g_cake, "grams cake flour =", g_apf, "grams APF +", g_corn, "grams cornstarch")


if __name__ == "__main__":
    main()
