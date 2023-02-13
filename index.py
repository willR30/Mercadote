#Python 3.11.1
#Flak 2.2.2
import requests
from flask import Flask, render_template, request


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

@app.route('/getProductByName',methods=["GET","POST"])
def getProductByName():
    if request.method=="POST":
        productName= request.form.get("txtProduct")
        print(f'Prodcut name: {productName}')

        api_url=f'https://api.escuelajs.co/api/v1/products/?title={productName}'
        response = requests.get(api_url).json()
        data={
            'product': response
        }
        
        try:
            return render_template('productFinded.html', data=data['product'][0])
        except Exception:
            return 'Error ty again later'
        

if __name__ == '__main__':
    app.run(debug=True)