import bs4
import requests

result = requests.get("https://www.filmaffinity.com/es/main.html")
sopa = bs4.BeautifulSoup(result.text, 'lxml')
prueba = sopa.select('.movie-card-13>a', href=True)

    
for i in prueba:
    try:
        result1 = requests.get(i['href'])
        sopa1 = bs4.BeautifulSoup(result1.text, 'lxml')
        title = sopa1.select("#main-title")[0].getText().strip()
        score = sopa1.select("#movie-rat-avg")[0].getText().strip().replace(",",".")
        image = sopa1.select("#movie-main-image-container>a>img")[0]['src'].strip()
        if float(score) > 7.0:
            print(f"{title} {score} {image}")
            img = requests.get(image)
            f = open(f'{title} {score}.jpg', 'wb')
            f.write(img.content)
            f.close()
    except IndexError or ValueError:
        continue
    

    