import pandas as pd
from joblib import load
knn2 = load('app/scripts/knn.joblib')
def calcular(alumnes):
    alumnes = pd.DataFrame(data=alumnes)
    pred=knn2.predict(alumnes)
    q=float(pred)
    if q - int(q)> 0.15:
        return int(q)+1
    elif q - int(q)<= 0.15:
        return int(q)
