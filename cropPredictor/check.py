import pickle

with open("static/models/cropPredictor.pkl", "rb") as file:
    obj = pickle.load(file)
    print(type(obj))
    print(obj)
