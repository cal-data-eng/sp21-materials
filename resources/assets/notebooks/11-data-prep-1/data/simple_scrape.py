import requests
import os
import sys
from bs4 import BeautifulSoup
from cprint import cprint

def _add_unique_postfix(fn):
    # __author__ = 'Denis Barmenkov <denis.barmenkov@gmail.com>'
    # __source__ = 'http://code.activestate.com/recipes/577200-make-unique-file-name/'
    if not os.path.exists(fn):
        return fn

    path, name = os.path.split(fn)
    name, ext = os.path.splitext(name)

    make_fn = lambda i: os.path.join(path, '%s(%d)%s' % (name, i, ext))

    for i in range(2, sys.maxsize):
        uni_fn = make_fn(i)
        if not os.path.exists(uni_fn):
            return uni_fn

    return None

def fetch_year(yyyy):
    prefix = f'monthly_precip_{yyyy}'
    output_dir = 'output'
    # html = requests.get('https://www.cnrfc.noaa.gov/monthly_precip_2020.php', timeout=3)
    print(f'Fetching https://www.cnrfc.noaa.gov/monthly_precip_{yyyy}.php')
    html = requests.get(f'https://www.cnrfc.noaa.gov/monthly_precip_{yyyy}.php', timeout=3)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table', class_='normal')
    print(f'Found {str(len(tables))} tables')
    # seqno = 1
    for t in tables:
        subdir = "output"
        try:
            os.mkdir(subdir)
            # if verbose:
            #     cprint("created directory " + subdir, c='c')
        except FileExistsError:
            pass
        filename = f'{subdir}/{prefix}.csv'
        out = open(_add_unique_postfix(filename), "w")
        cprint(f'created file  {filename}', c='c')
        rows = t.find_all('tr')
        for r in rows:
            # break when we see class="sortbottom" in a <tr> tag
            if r.has_attr('class') and 'sortbottom' in r['class']:
                break
            headers = r.find_all(['th'])
            thtd = r.find_all(['th','td'])
            txt = str([i.text.rstrip() for i in thtd])
            txt = txt.lstrip('[').rstrip(']')
            print(f'{yyyy}, {txt}', file = out)
        # seqno += 1

for yy in range(2002,2021):
    fetch_year(yy)