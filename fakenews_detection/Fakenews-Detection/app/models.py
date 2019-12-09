from django.db import models


# Create your models here.
class FormNews (models.Model):
    url = models.URLField()
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    predicao = models.FloatField(blank=True)

    def predict(self):
        # Import ML
        from keras.models import Sequential
        from keras.models import load_model
        from keras import layers
        from sklearn.model_selection import train_test_split
        from keras.utils import to_categorical
        from keras.preprocessing.sequence import pad_sequences
        from keras.preprocessing.text import Tokenizer
        from math import sqrt
        from sklearn.metrics import accuracy_score
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd

        # Constantes que usaremos em nosso código
        MAX_SEQUENCE_LENGTH = 5000
        MAX_NUM_WORDS = 25000
        TEXT_DATA = 'app/fake_or_real_news.csv'
        texto = self.texto


        # Leitura da base de dados e Limpeza dos dados (remover colunas de texto em branco, etc...)
        df = pd.read_csv(TEXT_DATA)
        df.drop(labels=['id', 'title'], axis='columns', inplace=True)
        mask = list(df['text'].apply(lambda x: len(x) > 0))
        df = df[mask]


        # Como utilizamos aprendiagem supervisionada separamos em dois dataframes um com os textos e outro com as labels (FAKE/REAL)
        texts = df['text']
        labels = df['label']


        # Criação dos tokens que iremos enviar para a rede convolucional
        tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
        tokenizer.fit_on_texts(texts)
        token_text = tokenizer.texts_to_sequences([texto])[0]
        text_padding = pad_sequences([token_text],
                                    maxlen=MAX_SEQUENCE_LENGTH,
                                    padding='pre',
                                    truncating='pre')

        # Leitura do modelo que foi salvo pelo outro arquivo
        model = load_model('app/model.h5')

       

        return 1 - model.predict(text_padding)[0][0]



    def save(self, *args, **kwargs):
        self.predicao = self.predict()
        super().save(*args, **kwargs)