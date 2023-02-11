import csv
import json

def convert_file(csv_file, json_file, model):
    with open(csv_file, encoding="utf-8") as csv_f:
        result = []
        for row in csv.DictReader(csv_f):
            record = {'model': model, "pk": row["id"]}
            del row['id']
            record['fields'] = row
            result.append(record)
            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

    with open(json_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False))

convert_file("ads.csv", "ads.json", "ads.ad")
convert_file("categories.csv", "categories.json", "ads.category")