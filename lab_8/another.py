import numpy as np
import tensorflow as tf

# Задаємо дані для тренування
# Приклад: логічне "або"
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
output_data = np.array([[0], [1], [1], [1]], dtype=np.float32)

# Визначаємо структуру нейронної мережі
model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, input_shape=(2,), activation='relu'),  # Прихований шар
    tf.keras.layers.Dense(1, activation='sigmoid')  # Вихідний шар
])

# Компілюємо модель
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Тренуємо модель
model.fit(input_data, output_data, epochs=1000, verbose=2)

# Перевіряємо результати
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
predictions = model.predict(test_data)
print("Predictions:")
print(predictions)
