from sklearn.linear_model import LogisticRegression
from utils.metrics import compute_performance


class LogisticReg(LogisticRegression):
    def __init__(self, df, classifier, max_iter=50,
                 class_weight='balanced',**kwargs):
        self.df = df.copy()
        self.classifier = classifier
        for gene in self.classifier:
            if gene not in self.df.columns:
                raise Exception(f"Gene {gene} not in dataframe")
        self.train_x = self.df[self.classifier]
        if 'response' not in self.df.columns:
            raise Exception("There is no response column")
        self.train_y = self.df['response']
        self.max_iter = max_iter
        self.class_weight = class_weight
        super().__init__(max_iter=self.max_iter,
                         class_weight=self.class_weight,
                         **kwargs)
        self.clf = self.fit(self.train_x,
                            self.train_y,
                            )

    def prediction(self, test_df) -> dict:
        if test_df is None:
           raise Exception("There is no test data")
        else: test_df = test_df.copy()
        test_x = test_df[self.classifier]


        prediction = self.clf.predict(test_x)
        prob_prediction = self.clf.predict_proba(test_x)[:,1]

        result_dict = {'Prediction' : prediction,
                       'Probability_Prediction' : prob_prediction,
                       }

        return result_dict

    def get_performance(self, valid_df=None) -> dict:
        if valid_df is None:
            valid_df = self.df
        else: valid_df = valid_df.copy()

        real_y = valid_df['response']
        pred_x = self.prediction(valid_df)['Prediction']
        pred_prob_x = self.prediction(valid_df)['Probability_Prediction']

        performance_dict = compute_performance(real_y, pred_x, pred_prob_x)

        return performance_dict

    def __str__(self):
        return (f'{self.__class__.__qualname__};'
                f'max_iter: {self.max_iter};'
                f'class_weight: {self.class_weight})')