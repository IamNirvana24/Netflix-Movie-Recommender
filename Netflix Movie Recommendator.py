from sklearn.cluster import KMeans

# 🎬 Features: Action, Horror, Sci-Fi, Romance, Suspense, Age Group
Movies_Data = [
    [90, 10, 10, 5, 80, 18],    # Action Thriller
    [10, 95, 10, 5, 90, 25],    # Horror Movie
    [30, 60, 30, 10, 70, 22],   # Horror-Action
    [85, 15, 5, 60, 60, 20],    # Action Romance
    [20, 20, 95, 15, 30, 23],   # Sci-Fi
    [25, 25, 30, 95, 35, 28],   # Romance Movie
    [88, 12, 12, 8, 75, 19],    # Action Thriller
    [12, 92, 15, 7, 88, 26],    # Horror
    [28, 65, 40, 12, 72, 21],   # Horror-Action
    [82, 18, 10, 65, 58, 19],   # Action Romance
    [18, 25, 92, 10, 35, 24],   # Sci-Fi
    [20, 20, 25, 90, 40, 30],   # Romance
]

# Train the KMeans model
model = KMeans(n_clusters=5, random_state=42)
model.fit(Movies_Data)

# 🎯 Test with a new movie
Testing_Model = [[82, 18, 12, 68, 55, 19]]
prediction = model.predict(Testing_Model)

# 🍿 Output recommendation using if-else
if prediction[0] == 0:
    print("💘 Romance Movie 💞")
elif prediction[0] == 1:
    print("👽 Sci-Fi Movie 🚀")
elif prediction[0] == 2:
    print("😱 Horror Movie 👻")
elif prediction[0] == 3:
    print("💥 Action Thriller 🔫")
elif prediction[0] == 4:
    print("❤️ Action Romance 🎬")
else:
    print("🎲 Unknown Movie Type")