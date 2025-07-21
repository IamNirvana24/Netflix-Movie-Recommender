# 🎬 Netflix Movie Recommender 🎯  
A Machine Learning model that recommends the **type of movie** (like Action Thriller, Romance, Sci-Fi, etc.) using unsupervised learning — powered by **KMeans Clustering**!

---

## 🍿 What It Does

Based on movie genre features (like Action, Horror, Romance, etc.), the model **clusters** similar movies together. When you give it a new movie with specific features, it will tell you what **kind of movie** it is — just like Netflix categories!

---

## 📊 Features Used

Each movie is described using the following **6 numerical features**:

| Feature    | Description                  | Range       |
|------------|------------------------------|-------------|
| 🎬 Action   | Intensity of action scenes   | 0 – 100     |
| 😱 Horror   | Level of horror/suspense     | 0 – 100     |
| 👽 Sci-Fi   | Sci-fi or futuristic content | 0 – 100     |
| 💞 Romance  | Romantic content             | 0 – 100     |
| 🕵️ Suspense | Mystery or thriller elements | 0 – 100     |
| 👤 Age Group| Average viewer age group     | 13 – 60     |

---

## 🤖 Machine Learning Model

- **Type**: Unsupervised Learning
- **Algorithm**: `KMeans` Clustering from `scikit-learn`
- **Clusters**: 5 clusters (groups) based on genre patterns

---

## 🧪 Example Test Case

```python
Testing_Model = [[82, 18, 12, 68, 55, 19]]

Made with ❤️ by [Nirvana Dubey] — part of my Machine Learning Projects Portfolio.
Follow me for more fun and beginner-friendly ML ideas!


