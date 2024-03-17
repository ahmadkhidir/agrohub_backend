import keras, os
import pandas as pd

"""Design a label preprocesssor with appropriate encoder and decoder functions"""

class LabelPreprocessor:
  save_path = "./labelpreprocessor"
  def __init__(self, label_df=None):
    self.lookup = keras.layers.StringLookup()
    if isinstance(label_df, pd.Series):
      self.lookup.adapt(label_df)
      if not os.path.exists(self.save_path):
        os.mkdir(self.save_path)
      self.lookup.save_assets(self.save_path)
      print(f"Assets Saved to: {self.save_path}")
    elif os.path.exists(os.path.join(self.save_path, "vocabulary.txt")):
      self.lookup.load_assets(self.save_path)
      print(f"Assets Loaded from: {self.save_path}")
    else:
      raise ValueError(f"Cannot access {self.save_path}")

  def encode(self, df):
    x = self.lookup(df)
    return x.numpy()

  def decode(self, multi_hots):
    vocab = self.lookup.get_vocabulary()
    result = []
    for item in multi_hots:
      result.append(vocab[item])
    return result


  @property
  def num_classes(self):
    return self.lookup.vocabulary_size()
