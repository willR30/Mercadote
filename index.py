#Python 3.11.1
#Flak 2.2.2

import requests
from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def home():
    data=getProducts()
    return render_template('home.html', data=data)
    #return render_template('layout.html')

@app.route('/categories')
def categories():
    data=getCategories()
    return render_template('categories.html',data=data)


def getProducts():
    api_url='https://api.escuelajs.co/api/v1/products'
    response = requests.get(api_url).json()
    data={
        'products': response
    }
    return data


def getCategories():
    api_url='https://api.escuelajs.co/api/v1/categories'
    response=requests.get(api_url).json()
    data={
        'categories': response
    }

    return data


if __name__ == '__main__':
    app.run(debug=True)