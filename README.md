# 🤖 Machine Learning

Repositorio de estudio y práctica de Machine Learning: desde el preprocesamiento y la limpieza de datos hasta el entrenamiento, la evaluación y la explicación de modelos, más una sección de Deep Learning.

Consolida varios repositorios de aprendizaje que tenía por separado. Cada uno conserva su historial de commits.

## Estructura

🌱 [**00. Fundamentos**](./00.Fundamentos/): CookBook (vectores y matrices, carga y limpieza de datos, datos numéricos y categóricos), validación cruzada, pipelines y funciones de scikit-learn

🔍 [**01. EDA**](./01.EDA/): selección de variables con clustering jerárquico

🧩 [**02. Modelos**](./02.Modelos/)
- Regresión: Housing, Medical
- Clasificación: árboles de decisión, Random Forest, Naive Bayes
- No supervisado: clustering y K-Means desde cero
- Supervivencia
- Sistemas de recomendación

💡 [**03. Explicabilidad**](./03.Model_Explanation/): SHAP values

📏 [**04. Evaluación**](./04.Model_Evaluation/): curvas ROC y YellowBrick

🧠 [**05. Deep Learning**](./05.Deep_Learning/)
- [Keras](./05.Deep_Learning/Keras/): redes neuronales, funciones de activación, clasificación binaria y múltiple, regresión
- [PyTorch](./05.Deep_Learning/PyTorch/): tensores, datasets y redes neuronales
- [Google ML Crash Course](./05.Deep_Learning/Google_ML_Crash_Course/): regresión lineal con TensorFlow

🎓 [**06. Cursos**](./06.Cursos/)
- [scikit-learn profesional](./06.Cursos/scikit-learn-professional/): PCA, regularización, datos atípicos, ensambles, no supervisado, validación, optimización de hiperparámetros y despliegue del modelo con una API
- [Clasificación](./06.Cursos/ML_Clasificacion/): regresión logística, árboles y Telco Churn
- [Applied Machine Learning in Python](./06.Cursos/Applied_ML_Coursera/) (Coursera, Universidad de Michigan): `adspy_shared_utilities.py` es material del curso
- [Fullstack Data Scientist](./06.Cursos/Fullstack_Data_Scientist/): EDA, ETL, ANOVA, segmentación RFM con K-Means, LIME y SHAP

🛠️ [**utils**](./utils/): funciones auxiliares para EDA y modelado

## Uso

```bash
pip install -r requirements.txt
```

Los datasets no se versionan (`*.csv` está en `.gitignore`); los notebooks los esperan en `Data/Raw/`. Algunas carpetas de `05.Deep_Learning` y `06.Cursos` traen su propio archivo de entorno.
