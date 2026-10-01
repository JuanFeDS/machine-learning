from utils import Utils
from models import Models

utils = Utils()
models = Models()

def app():

    data = utils.load_from_csv('data/felicidad.csv')
    
    X, y = utils.features_target(data, ['country', 'rank', 'score'], 'score')

    models.grid_training(X, y)


if __name__ == '__main__':
    app()