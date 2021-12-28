from application import app
from application.forms import RegionForm
from flask import render_template, request, redirect, url_for
import requests

backend = "backend:5000"


columns = [
    {
        "field": "region_id",
        "title": "ID",
        "sortable": True,
    },
    {
        "field": "region_name",
        "title": "Region",
        "sortable": True,
    },
    {
        "field": "region_property_address",
        "title": "Property Address",
        "sortable": True,
    },
    {
        "field": "region_price",
        "title": "Price",
        "sortable": True,
    },
    {
        "field": "description",
        "title": "Description",
        "sortable": True,
    }
]


@app.route('/')
@app.route('/home')
def home():
    all_regions = requests.get(f"http://{backend}/regions").json()
    app.logger.info(all_regions)

    data = []
    for region in all_regions:
        app.logger.info(region)
        data.append(
            {
                "region_id":  region["region_id"],
                "region_name": region["region_name"],
                "region_property_address": region["region_property_address"],
                "region_price": region["region_price"],
                "description": region["description"],
            }
        )
        app.logger.info(data)

    return render_template('index.html',  data=data,
                           columns=columns)


@app.route('/add', methods=['GET', 'POST'])
def create_region():
    form = RegionForm()
    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/add",
            json={
                "region_name": form.region_name.data,
                "region_property_address": form.region_property_address.data,
                "region_price": form.region_price.data,
                "description": form.description.data,
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for('home'))

    return render_template("create_region.html", title="Create Region", form=form)


@app.route('/delete/<int:id>')
def delete_region(id):
    response = requests.delete(f"http://{backend}/delete/{id}")
    return redirect(url_for('home'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_region(id):
    form = RegionForm()
    region = requests.get(f"http://{backend}/region/{id}").json()

    if request.method == "POST":
        response = requests.put(f"http://{backend}/update/{id}",
                                json={
                                    "region_name": form.region_name.data,
                                    "region_property_address": form.region_property_address.data,
                                    "region_price": form.region_price.data,
                                    "description": form.description.data,
                                }
                                )
        return redirect(url_for('home'))

    return render_template('update_region.html', region=region, form=form)
