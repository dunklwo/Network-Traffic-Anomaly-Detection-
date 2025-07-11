import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# STEP 1: Load the 5-tuple log
df = pd.read_csv("five_tuple_log.csv")

# STEP 2: Preprocess the data
# Encode IP addresses and protocol to numeric
le_ip = LabelEncoder()
df['src_ip'] = le_ip.fit_transform(df['src_ip'])
df['dst_ip'] = le_ip.fit_transform(df['dst_ip'])
df['protocol'] = df['protocol'].map({'TCP': 0, 'UDP': 1}).fillna(2)

# Drop timestamp (not needed for model)
df.drop('timestamp', axis=1, inplace=True)

# STEP 3: Define feature set
X = df[['src_ip', 'dst_ip', 'src_port', 'dst_port', 'protocol']]

# STEP 4: Train an unsupervised anomaly detection model
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(X)

# STEP 5: Predict anomalies
df['anomaly'] = model.predict(X)  # -1 = anomaly, 1 = normal

# STEP 6: Show results
anomalies = df[df['anomaly'] == -1]
print("📌 Detected anomalies:")
print(anomalies)

# Optional: Save to CSV
df.to_csv("five_tuple_with_anomaly.csv", index=False)
print("✅ All predictions saved to five_tuple_with_anomaly.csv")

import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Separate normal and anomalies
normal = df[df['anomaly'] == 1]
anomalies = df[df['anomaly'] == -1]

# Plot: src_port vs dst_port
plt.figure(figsize=(10, 6))
plt.scatter(normal['src_port'], normal['dst_port'], 
            c='green', label='Normal', alpha=0.6)
plt.scatter(anomalies['src_port'], anomalies['dst_port'], 
            c='red', label='Anomaly', marker='x', s=80)

plt.xlabel("Source Port")
plt.ylabel("Destination Port")
plt.title("Network Traffic Anomaly Detection (5-Tuple)")
plt.legend()
plt.tight_layout()
plt.savefig("anomaly_plot.png")
plt.show()
