from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt


def image_segmentation(image_path, num_clusters, save_path=None):
    # Зчитуємо зображення
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Перетворюємо зображення в одновимірний масив пікселів
    pixels = image.reshape((-1, 3))

    # Застосовуємо K-Means кластеризацію
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)

    # Отримуємо мітки для кожного пікселя
    labels = kmeans.labels_

    # Відновлюємо форму оригінального зображення
    segmented_image = labels.reshape(image.shape[:2])

    # Відображаємо результат
    plt.imshow(segmented_image, cmap='viridis')
    plt.axis('off')

    # Зберігаємо або відображаємо зображення
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        print(f"Segmented image saved to {save_path}")
    else:
        plt.show()


# Приклад виклику функції з збереженням у файл
image_segmentation('cat-2.jpg', num_clusters=4, save_path='segmented_image.png')
