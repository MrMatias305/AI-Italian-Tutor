from data.sample_lesson import lessons
from embedding import create_embedding

for i, lesson in enumerate(lessons):
    embedding = create_embedding(lesson['content'])
    print(f"Topic {i+1}: ", lesson["topic"])
    print("Embedding length: ", len(embedding))
    print("First 5 values: ", embedding[:5])
    print('-'*40)