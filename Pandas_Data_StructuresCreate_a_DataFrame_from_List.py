import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Example Usage:
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

df = createDataframe(student_data)
print(df)
