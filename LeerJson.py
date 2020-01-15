# -*- coding: utf-8 -*-
import json

if __name__ == "__main__":
        with open('package.json') as file:
            data=json.load(file)
        print(data)
        print("\n")
        print(data['devDependencies'])