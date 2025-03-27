import os
import json
import csv
import xml.etree.ElementTree as ET
import yaml

class FileReader:
    def __init__(self, base_path="../../datasets"):
        self.base_path = base_path

    def read_file(self, filename):
        full_path = os.path.join(self.base_path, filename)
        with open(full_path, "r") as file:
            return file.read()

    def read_txt(self):
        return self.read_file("product.txt")

    def read_csv(self):
        full_path = os.path.join(self.base_path, "product.csv")
        with open(full_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def read_json(self):
        full_path = os.path.join(self.base_path, "product.json")
        with open(full_path, "r") as file:
            return json.load(file)

    def read_xml(self):
        full_path = os.path.join(self.base_path, "product.xml")
        tree = ET.parse(full_path)
        return tree.getroot()

    def read_yaml(self):
        full_path = os.path.join(self.base_path, "product.yaml")
        with open(full_path, "r") as file:
            return yaml.safe_load(file)

if __name__ == "__main__":
    reader = FileReader()
    print("TXT Data:", reader.read_txt())
    print("CSV Data:", reader.read_csv())
    print("JSON Data:", reader.read_json())
    print("XML Data:", reader.read_xml())
    print("YAML Data:", reader.read_yaml())
