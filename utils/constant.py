import os

def define_constants(
        base_dir: str = './dst',
        dst_file: str = 'dataset.csv',
        val_file: str = None,
        test_file: str = None,
        src_path: str = './src',
        src_file: str = 'result.csv'
):
    dataset_file = os.path.join(base_dir, dst_file)
    result_file = os.path.join(src_path, src_file)

    if val_file is None:
        validation_file = None
    else:
        validation_file = os.path.join(base_dir, val_file)

    if test_file is None:
        test_file = None
    else:
        test_file = os.path.join(base_dir, test_file)

    return {
        'dataset_path' : dataset_file,
        'validation_path' : validation_file,
        'result_path' : result_file,
        'test_path' : test_file,
    }