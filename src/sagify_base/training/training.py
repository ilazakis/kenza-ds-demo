import os
        
from sagify.api.hyperparameter_tuning import log_metric
from sklearn.externals import joblib
        
from iris_training import train as training_logic


def train(input_data_path, model_save_path, hyperparams_path=None):
    """
    The function to execute the training.

    :param input_data_path: [str], input directory path where all the training file(s) reside in
    :param model_save_path: [str], directory path to save your model(s)
    :param hyperparams_path: [optional[str], default=None], input path to hyperparams json file.
    Example:
        {
            "max_leaf_nodes": 10,
            "n_estimators": 200
        }
    """
    input_file_path = os.path.join(input_data_path, 'iris.data')
    clf, accuracy = training_logic(input_file_path=input_file_path, hyperparams_path=hyperparams_path)
        
    output_model_file_path = os.path.join(model_save_path, 'model.pkl')
    joblib.dump(clf, output_model_file_path)
        
    log_metric("Accuracy", accuracy)