from application import app, db
from application.models import Regions
from flask import request, jsonify, Response


@app.route('/regions', methods=['GET'])
def read_all_regions():
    all_regions = Regions.query.all()
    dict = []
    for region in all_regions:
        dict.append(
            {
                "region_id": region.region_id,
                "region_name": region.region_name,
                "region_property_address": region.region_property_address,
                "region_price": region.region_price,
                "description": region.description,
            }
        )
    return jsonify(dict)


@app.route('/region/<int:id>', methods=['GET'])
def get_region(id):
    region = Regions.query.get(id)
    dict = {
        "region_id": region.region_id,
        "region_name": region.region_name,
        "region_property_address": region.region_property_address,
        "region_price": region.region_price,
        "description": region.description,
    }
    return jsonify(dict)


@app.route('/add', methods=['POST'])
def create_region():
    package = request.json
    new_region = Regions(region_name=package["region_name"], region_property_address=package["region_property_address"],
                         region_price=package["region_price"], description=package["description"])
    db.session.add(new_region)
    db.session.commit()
    return "Region added to database"


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_region(id):
    regions = Regions.query.get(id)
    db.session.delete(regions)
    db.session.commit()
    return Response(f"Deleted region with ID: {id}", mimetype='text/plain')


@app.route('/update/<int:id>', methods=['PUT'])
def update_region(id):
    package = request.json
    region = Regions.query.get(id)
    region.region_name = package["region_name"]
    region.region_property_address = package["region_property_address"]
    region.region_price = package["region_price"]
    region.description = package["description"]
    db.session.commit()
    return Response(f"Updated task (ID: {id})", mimetype='text/plain')
