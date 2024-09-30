import sklearn.metrics as metrics
import numpy as np


def compute_performance(real_y, pred_y, prob):
    performance = dict()
    performance['AUC'] = float(metrics.roc_auc_score(real_y, prob))
    performance['PRAUC'] = float(metrics.average_precision_score(real_y, prob))
    performance['accuracy'] = float(metrics.accuracy_score(real_y, pred_y))
    performance['precision'] = float(metrics.precision_score(real_y, pred_y))
    performance['recall'] = float(metrics.recall_score(real_y, pred_y))
    performance['f1'] = float(metrics.f1_score(real_y, pred_y))
    performance['mcc'] = float(metrics.matthews_corrcoef(real_y, pred_y))
    performance['R2'] = float(metrics.r2_score(real_y, prob))

    return performance