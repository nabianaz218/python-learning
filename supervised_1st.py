import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
df = pd.read_csv("data.csv")
# Drop the ID column immediately
df = df.drop('customerID', axis=1)

# Fix the numeric column
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
# This ensures you only pick the ones that are actually text
cat_cols = df.select_dtypes(include=['object']).columns
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)
all_numeric = df_encoded.select_dtypes(include=['int64', 'float64']).columns
cols_to_scale = [col for col in all_numeric if df_encoded[col].nunique() > 2]
sd = StandardScaler()
df_encoded[cols_to_scale] = sd.fit_transform(df_encoded[cols_to_scale])
X = df_encoded.drop(['Churn_Yes'], axis=1)
y = df_encoded['Churn_Yes'].astype(int)
X_trian , X_test , y_trian , y_test = train_test_split(X,y ,test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_trian,y_trian)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
# Get probabilities
y_probs = model.predict_proba(X_test)[:, 1]

# Plot distribution of probabilities
plt.hist(y_probs, bins=20)
plt.title("Distribution of Churn Probabilities")
plt.xlabel("Probability of Churn")
plt.ylabel("Number of Customers")
plt.show()
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).sort_values().plot(kind='barh', color='teal')
plt.title("Top Factors Influencing Churn")
plt.show()