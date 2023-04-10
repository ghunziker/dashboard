import pandas as pd
import os
import logging
from ..models import ArticleMaster, PassengerNumbers

def import_master(file):
    master_cnames = ["location_id",
                "article_nr",
                "article_desc",
                "item_status",
                "UOM",
                "category_id",
                "category_desc",
                "class_id",
                "class_desc",
                "subclass_id",
                "subclass_desc",
                "brand_id",
                "brand_desc",
                "unitcost",
                "supplier_id",
                "supplier_desc",
                "leadtime",
                "minstock",
                "lotsize",
                "actualstock",
                "undefined",
                "minorder_qty"]
    master = pd.read_csv(file, sep="\t", names=master_cnames, usecols=list(range(0, 22)))
    for index, row in master.iterrows():
        try:
            instance = ArticleMaster.objects.get(location_id=row["location_id"], article_nr=row["article_nr"])
            if not pd.isnull(row.get("article_desc")):
                instance.article_desc = row.get("article_desc", None)
            if not pd.isnull(row.get("item_status")):
                instance.item_status = row.get("item_status", None)
            if not pd.isnull(row.get("UOM")):
                instance.UOM = row.get("UOM", None)
            if not pd.isnull(row.get("category_id")):
                instance.category_id = row.get("category_id", None)
            if not pd.isnull(row.get("category_desc")):
                instance.category_desc = row.get("category_desc", None)
            if not pd.isnull(row.get("class_id")):
                instance.class_id = row.get("class_id", None)
            if not pd.isnull(row.get("class_desc")):    
                instance.class_desc = row.get("class_desc", None)
            if not pd.isnull(row.get("subclass_id")):
                instance.subclass_id = row.get("subclass_id", None)
            if not pd.isnull(row.get("subclass_desc")):
                instance.subclass_desc = row.get("subclass_desc", None)
            if not pd.isnull(row.get("brand_id")):    
                instance.brand_id = row.get("brand_id", None)
            if not pd.isnull(row.get("brand_desc")):
                instance.brand_desc = row.get("brand_desc", None)
            if not pd.isnull(row.get("unitcost")):
                instance.unitcost = row.get("unitcost", None)
            if not pd.isnull(row.get("supplier_id")):
                instance.supplier_id = row.get("supplier_id", None)
            if not pd.isnull(row.get("supplier_desc")):
                instance.supplier_desc = row.get("supplier_desc", None)
            if not pd.isnull(row.get("leadtime")):
                instance.leadtime = row.get("leadtime", None)
            if not pd.isnull(row.get("minstock")):
                instance.minstock = row.get("minstock", None)
            if not pd.isnull(row.get("lotsize")):
                instance.lotsize = row.get("lotsize", None)
            if not pd.isnull(row.get("undefined")):
                instance.undefined =  row.get("undefined", None)
            if not pd.isnull(row.get("minorder_qty")):
                instance.minorder_qty =  row.get("minorder_qty", None)
            instance.save()
        except ArticleMaster.DoesNotExist:
            instance = ArticleMaster(
                location_id=row["location_id"],
                article_nr=row["article_nr"],
                article_desc=row.get("article_desc", None) if not pd.isnull(row.get("article_desc")) else None,
                item_status=row.get("item_status", None) if not pd.isnull(row.get("item_status")) else None,
                UOM=row.get("UOM", None) if not pd.isnull(row.get("UOM")) else None,
                category_id=row.get("category_id", None) if not pd.isnull(row.get("category_id")) else None,
                category_desc=row.get("category_desc") if not pd.isnull(row.get("category_desc")) else None,
                class_id=row.get("class_id", None) if not pd.isnull(row.get("class_id")) else None,
                class_desc=row.get("class_desc", None) if not pd.isnull(row.get("class_desc")) else None,
                subclass_id=row.get("subclass_id", None) if not pd.isnull(row.get("subclass_id")) else None,
                subclass_desc=row.get("subclass_desc", None) if not pd.isnull(row.get("subclass_desc")) else None,
                brand_id=row.get("brand_id", None) if not pd.isnull(row.get("brand_id")) else None,
                brand_desc=row.get("brand_desc", None) if not pd.isnull(row.get("brand_desc")) else None,
                unitcost = row.get("unitcost", None) if not pd.isnull(row.get("unitcost")) else None,
                supplier_id = row.get("supplier_id", None) if not pd.isnull(row.get("supplier_id")) else None,
                supplier_desc = row.get("supplier_desc", None) if not pd.isnull(row.get("supplier_desc")) else None,
                leadtime = row.get("leadtime", None) if not pd.isnull(row.get("leadtime")) else None,
                minstock = row.get("minstock", None) if not pd.isnull(row.get("minstock")) else None,
                lotsize = row.get("lotsize", None) if not pd.isnull(row.get("lotsize")) else None,
                undefined =  row.get("undefined", None) if not pd.isnull(row.get("undefined")) else None,
                minorder_qty =  row.get("minorder_qty", None) if not pd.isnull(row.get("minorder_qty")) else None
                )
            instance.save()

def import_passenger(file):
    passengernumbers = pd.read_csv(file, sep="\t", names=["date", "passengers", "location_id"])
    passengernumbers["location_id"] = passengernumbers["location_id"].fillna(value=621)
    passengernumbers["date"] = pd.to_datetime(passengernumbers["date"])
    passengernumbers.sort_values(by="date")
    passengernumbers = passengernumbers.reset_index(drop=True)
    for index, row in passengernumbers.iterrows():
        try:
            instance = PassengerNumbers.objects.get(date=row["date"], location_id=row["location_id"])
            if not pd.isnull(row.get("passengers")):
                instance.article_desc = row.get("passengers", None)
            instance.save()
        except PassengerNumbers.DoesNotExist:
            instance = PassengerNumbers(
                location_id=row.get("location_id", None) if not pd.isnull(row.get("location_id")) else None,
                date=row.get("date"),
                passengers=row.get("passengers", None) if not pd.isnull(row.get("passengers")) else None
                )
            instance.save()


if __name__ == "__main__":
    pass