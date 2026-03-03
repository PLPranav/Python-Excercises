import numpy as np

#Task 1: Generate and Inspect the Data
np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))

print("Full Scores Array:\n", scores)
print(f"\n3rd student, 2nd subject: {scores[2, 1]}")
print("Last 2 students' scores:\n", scores[-2:])
print("First 3 students, subjects 2 & 3:\n", scores[:3, 1:3])


#Task 2: Analyze with Broadcasting
subject_means = np.round(scores.mean(axis=0), 2)
print(f"\nAverage score per subject: {subject_means}")

curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

curved_scores = np.clip(curved_scores, None, 100)
print("Curved Scores (Clipped at 100):\n", curved_scores)

student_max = curved_scores.max(axis=1)
print(f"Best score per student: {student_max}")


#Task 3: Normalize and Identify
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized_scores = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized Scores (0-1 scale):\n", normalized_scores)

max_idx_flat = np.argmax(normalized_scores)
student_idx, subject_idx = np.unravel_index(max_idx_flat, normalized_scores.shape)
print(f"Highest normalized value at: Student {student_idx}, Subject {subject_idx}")

high_scores = curved_scores[curved_scores > 90]
print(f"Curved scores strictly above 90: {high_scores}")