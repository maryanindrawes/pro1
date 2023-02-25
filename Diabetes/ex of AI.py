import pandas as pd
from keras import Sequential
from keras.layers import InputLayer, Dense
from sklearn.model_selection import train_test_split
import tensorflow

df = pd.read_csv("diabetes.csv")
train_df, test_df = train_test_split(df, test_size=0.20)

train_df = pd.DataFrame(train_df)
train_X = train_df.drop(columns=["Outcome"])
train_Y = train_df["Outcome"]

model = Sequential()
model.add(InputLayer(input_shape=train_X.shape[1]))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
model.fit(train_X, train_Y, epochs=20)


