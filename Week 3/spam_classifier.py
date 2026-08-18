import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data=pd.read_csv("spam_dataset.csv")

X=data["message"]
y=data["label"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

vectorizer=TfidfVectorizer()

X_train=vectorizer.fit_transform(X_train)
X_test=vectorizer.transform(X_test)

model=MultinomialNB()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("Actual:")
print(y_test.values)

print("Predicted:")
print(prediction)

print("Accuracy:",accuracy_score(y_test,prediction))

message=["You won a free prize"]
message=vectorizer.transform(message)

result=model.predict(message)

print("New Message:",result[0])