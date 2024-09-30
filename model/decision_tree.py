import graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from utils.metrics import compute_performance


class Decision_tree(DecisionTreeClassifier):
    def __init__(self, df, classifier,
                 max_depth=3,
                 min_samples_leaf=3,
                 class_weight='balanced',
                 random_state=42,
                 **kwargs):
        self.df = df.copy()
        self.classifier = classifier
        for gene in self.classifier:
            if gene not in self.df.columns:
                raise Exception(f"Gene {gene} not in dataframe")
        self.train_x = self.df[self.classifier]
        if 'response' not in self.df.columns:
            raise Exception("There is no response column")
        self.train_y = self.df['response']
        self.max_depth = max_depth
        self.min_samples_leaf = min_samples_leaf
        self.class_weight = class_weight
        self.random_state = random_state
        super().__init__(max_depth=self.max_depth,
                         min_samples_leaf=self.min_samples_leaf,
                         class_weight=self.class_weight,
                         random_state=self.random_state,
                         **kwargs)
        self.clf = self.fit(self.train_x,
                            self.train_y)

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
# Absolute path preferred. Graphviz package doesn't work out well in virtual environment.
    def get_tree_image(self, file_name='tree', directory='./', format='png'):
        dot_data = export_graphviz(self.clf,
                                   out_file=None,
                                   feature_names=self.train_x.columns,
                                   proportion=True,
                                   class_names=['0', '1',],
                                   filled=True,
                                   rounded=True,
                                   special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render(filename=file_name, directory=directory, format=format)
        return graph
    def __str__(self):
        return (f'{self.__class__.__qualname__}; '
                f'max_depth: {self.max_depth}; '
                f'min_samples_leaf: {self.min_samples_leaf}; '
                f'random_state: {self.random_state})')