import opendatasets as od
import zipfile

# download data from kaggle
od.download(
    'https://www.kaggle.com/datasets/jessicali9530/celeba-dataset', force=True)

Dataset = "celeba-dataset"
with zipfile.ZipFile("./celeba-dataset/"+Dataset+".zip", "r") as z:
    z.extractall(".")
