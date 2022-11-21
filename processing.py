import pandas as pd


def do_calculation(number1, number2):
    return number1 + number2

def cake_flour(g_cake):
    ratio_apf = 105./120
    ratio_corn = 14./120

    g_apf = g_cake * ratio_apf
    g_corn = g_cake * ratio_corn

    return  '{} grams cake flour =<br> {}g APF + {}g cornstarch'.format(g_cake, g_apf, g_corn)

def df_html_formatting(df):
    #return (df.head())
    return df.to_html()

def main_get_ingredient_recipes(ingredient):
    pd.set_option('display.max_colwidth', -1)

    df = pd.read_csv(r'/home/acooknbook/mysite/simpledb.csv')

    return df_html_formatting(df[df['Ingredients'].str.contains(ingredient, case=False)])


