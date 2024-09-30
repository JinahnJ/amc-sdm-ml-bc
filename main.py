import pandas as pd
import yaml
from model.logiReg import LogisticReg
from utils.constant import define_constants
from classifier.classifier import classifier_dict
from model.decision_tree import Decision_tree
from model.random_forest import Random_Forest
from utils.export_result import export_result
from utils.scaler import df_scaler
import argparse

if __name__ == '__main__':
    #parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", "-c",
                        type=str,
                        help="config file path, usually ./config/config.yaml")
    pars_args = parser.parse_args()
    pars_args = vars(pars_args)
    with open(pars_args['config_path'], 'r') as f:
        args = yaml.load(f, Loader=yaml.FullLoader)

    dic_path = define_constants(
        base_dir=args['base_dir'],
        dst_file=args['dataset_file_name'],
        val_file=args['validation_file_name'],
        src_path=args['result_dir_path'],
        src_file=args['result_file_name'],
        test_file=args['test_file_name'],)

    train_df = pd.read_csv(dic_path['dataset_path'])
    train_df_scaled = df_scaler(train_df, response_column_name='response')

    if dic_path['validation_path'] is None:
        pass
    else:
        validation_df = pd.read_csv(dic_path['validation_path'])
        validation_df_scaled = df_scaler(validation_df, response_column_name='response')

    if dic_path['test_path'] is None:
        pass
    else:
        test_df = pd.read_csv(dic_path['test_path'])
        test_df_scaled = df_scaler(test_df)

    classifier = classifier_dict[args['classifier']]

    if args['model'] == 'LR':
        model = LogisticReg(train_df_scaled, classifier)
    elif args['model'] == 'DT':
        model = Decision_tree(train_df_scaled, classifier)
    elif args['model'] == 'RF':
        model = Random_Forest(train_df_scaled, classifier)
    else: raise ValueError('Model type not supported')

    if args['test_file_name'] is not None:
        predict_dict = model.prediction(test_df=test_df_scaled)
    else:
        predict_dict = {}
        predict_dict.setdefault('Prediction', None)
        predict_dict.setdefault('Probability_Prediction', None)
    performance = model.get_performance(valid_df=validation_df_scaled)

    export_result(dic_path, model,
                  performance,
                  predict_dict['Prediction'],
                  predict_dict['Probability_Prediction'])


    if args['model'] in ('DT', 'RF'):
        model.get_tree_image(directory=args['result_dir_path'])

    print('Done')



