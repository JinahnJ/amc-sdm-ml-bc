
import yaml
from pathlib import Path

def export_result(dict_path, model,
                   performance,
                   prediction_result,
                   probability_prediction_result,
                   src_path='./src',
                   result_name='result.yaml', **kwargs):
    yaml_data = [
        {
            "dataset_path" : dict_path["dataset_path"],
            "validation_path" : dict_path["validation_path"],
            "test_path" : dict_path["test_path"],
            "result_path" : dict_path["result_path"],
        },
        {
            "model": str(model),
            "classifier": str(model.classifier),
        },
        {
            "performance": str(performance)
        },
        {
            "prediction_result": str(prediction_result),
            "probability_prediction_result": str(probability_prediction_result),
        },
    ]
    result_path = Path(src_path) / result_name
    result_path.touch(exist_ok=True)
    with open(result_path, 'w+') as f:
        yaml.dump(yaml_data, f)
