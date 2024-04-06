import requests
import csv

from .models import Collection, Owner, Contract, CollectionItem


def fetch_all_results(max_records=300):
    all_results = []
    url = "https://api.opensea.io/api/v2/collections"
    headers = {
        "accept": "application/json",
        "x-api-key": "4d54011a2474489ebc919837c276ac34"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    next = data['next']
    batch = 0
    total_records_fetched = len(data['collections'])

    while next and total_records_fetched < max_records:
        batch = batch+1
        print(f"Fetching Records for the batch {batch}")
        params = {"next": next, "chain": "ethereum"}
        response = requests.get(url, headers=headers, params=params)

        data = response.json()
        results = data['collections']
        all_results.extend(results)
        total_records_fetched += len(results)

        # Check if there's a 'next' attribute
        if 'next' in data and total_records_fetched < max_records:
            next = data['next']
        else:
            next = None

    return all_results[:max_records]  # Trim the results to the max_records limit


def transform(collections):
    data_lake_entries = []
    for each_collection in collections:
        data_lake_entry = {}
        data_lake_entry.update({"collection": each_collection.get("collection")})
        data_lake_entry.update({"name": each_collection.get("name")})
        data_lake_entry.update({"description": each_collection.get("description")})
        data_lake_entry.update({
            "image_url": each_collection.get("image_url")})
        data_lake_entry.update({
            "owner": each_collection.get("owner")})
        data_lake_entry.update({
            "twitter_username": each_collection.get("twitter_username")})

        contracts = each_collection.get("contracts")
        data_lake_entry.update({"contracts": contracts})

        data_lake_entries.append(data_lake_entry)

    return data_lake_entries


def load(data):
    # Create Collection objects
    for row in data[1:]:
        collection = Collection.objects.create(name=row['collection'])
        collection_item = CollectionItem.objects.create(
            collection=collection,
            name=row['name'],
            description=row['description'],
            image_url=row['image_url'],
            twitter_username=row['twitter_username']
        )
        for a in list(row.get("contracts", [])):
            contract = Contract.objects.create(
                address=a['address'],
                chain=a['chain']
            )
            collection_item.contracts.add(contract)

        owner = Owner.objects.create(
            name=row['owner']
        )
        collection.owner = owner
        collection_item.save()
        collection.save()


def write_dicts_to_csv(data):
    # Extract column headers from the keys of the first dictionary
    headers = data[0].keys()
    file_path = "data_lake.csv"

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        # Write header row
        writer.writeheader()

        # Write data rows
        for row in data:
            writer.writerow(row)


# raw_records = fetch_all_results(300)
# transformed_data = utils.transform(raw_records)
# write_dicts_to_csv(transformed_data)
# load(transformed_data)
