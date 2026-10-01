import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sklearn
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def run():

    # Preparación de los datos
    
    df = pd.read_csv('./data/heart.csv')

    features = df.drop(['target'], axis =1)
    features = StandardScaler().fit_transform(features)
    
    target = df['target']


    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3) 

    # Construcción del algoritmo PCA
    
    # Utilizando PCA
    pca = PCA(n_components = 5)
    pca.fit(X_train)

    varianza = pca.explained_variance_
    ratio = pca.explained_variance_ratio_

    # print(pca.explained_variance_)
    varianza = np.array(varianza.reshape(-1,1))
    ratio = ratio.reshape(-1,1)

    # print(varianza, ratio)

    # tabla = pd.DataFrame(varianza)
    # print(tabla)

    array_1 = np.array([1,2,3,4,5]).reshape(-1, 1)
    array_2 = np.array([5,2,3,4,5]).reshape(-1, 1)

    print(array_1[0], array_2)

    # daf = pd.DataFrame([array_1, array_2])
    # print(daf)

    # plt.plot(range(len(pca.explained_variance_)), pca.explained_variance_ratio_)
    # plt.show()

    # Utilizando IPCA
    ipca = IncrementalPCA(n_components = 5, batch_size = 10)
    ipca.fit(X_train)

    # plt.plot(range(len(ipca.explained_variance_)), ipca.explained_variance_ratio_)
    # plt.show()


    # Construimos el aloritmo de regresión logistica