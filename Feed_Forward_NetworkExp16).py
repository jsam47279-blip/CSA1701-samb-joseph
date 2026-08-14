from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.3,
    random_state=42
)

y_train = to_categorical(y_train, 3)
y_test_cat = to_categorical(y_test, 3)

model = Sequential([
    Dense(
        10,
        input_dim=4,
        activation='relu'
    ),
    Dense(
        3,
        activation='softmax'
    )
])

model.compile(
    loss='categorical_crossentropy',
    optimizer='sgd',
    metrics=['accuracy']
)

model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=10,
    verbose=0
)

loss, accuracy = model.evaluate(
    X_test,
    y_test_cat,
    verbose=0
)

print(
    f"Accuracy: {accuracy*100:.2f}%"
)
