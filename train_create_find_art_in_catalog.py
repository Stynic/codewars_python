# мы сделали изменение
You are given a small extract of a catalog:

s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

...
(prx stands for price, qty for quantity) and an article i.e "saw".

The function catalog(s, "saw") returns the line(s) corresponding to the article with $ before the prices:

"table saw > prx: $1099.99 qty: 5\nsaw > prx: $9 qty: 10\n..."
If the article is not in the catalog return "Nothing".

import re

def catalog(s, article):
    str_pattr = ''
    pattern = re.compile(f'<prod><name>.*{article}.*</name>.*</prod>')
    list_article = re.findall(pattern, s)
    if list_article:
        last_art = len(list_article)
        count = 0
        for art in list_article:
            price = re.search(r"\d+[.]?[\d]*", re.search(r"<prx>.*</prx>", art).group(0)).group(0)if re.search(r"<prx>.*</prx>", art).group(0)!= None else ''
            name = re.sub(r'<name>|</name>', '', re.search(r"<name>.*</name>", art).group(0)) if re.search(r"<name>.*</name>", art).group(0)!= None else ''
            quantity = re.search(r"\d+", re.search(r"<qty>.*</qty>", art).group(0)).group(0) if re.search(r"<qty>.*</qty>", art) != None else ''
            str_pattr += f'{name} > prx: ${price} qty: {quantity}' if len(list_article) == 1 or count == last_art - 1 else f'{name} > prx: ${price} qty: {quantity}\r\n'
            count += 1
    else:
        str_pattr = 'Nothing'
    return str_pattr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = """<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

    <prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

    <prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

    <prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

    <prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

    <prod><name>chair</name><prx>100</prx><qty>20</qty></prod>

    <prod><name>fan</name><prx>50</prx><qty>8</qty></prod>

    <prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>

    <prod><name>battery</name><prx>150</prx><qty>12</qty></prod>

    <prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>

    <prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>

    <prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>

    <prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>

    <prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>

    <prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>

    <prod><name>platform</name><prx>65</prx><qty>21</qty></prod>

    <prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>

    <prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>

    <prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>

    <prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>

    <prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>

    <prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>

    <prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>

    <prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>"""
    print(catalog(s, 'ladder'))
    print(catalog(s, 'saw'))
    print(catalog(s, 'wood pallet'))
