# Network-Traffic-Anomaly-Detection-

# 🛡️ Behavioral Network Intrusion Detection System

A behavioral-based Network Intrusion Detection System (NIDS) that captures live network traffic, analyzes 5-tuple features, and uses unsupervised machine learning (Isolation Forest) to detect suspicious or anomalous activity.

---

## 📌 Objective

This project aims to develop a lightweight NIDS that doesn't rely on signature-based detection. Instead, it uses a machine learning model trained on normal traffic behavior to identify deviations such as port scanning, DNS abuse, or suspicious external access.

---

## ⚙️ Features

- 📡 Real-time Packet Capture:** Uses Scapy to capture live packets and extract 5-tuple information (`src_ip`, `dst_ip`, `src_port`, `dst_port`, `protocol`).
- 🧠 Behavioral Detection with ML:** Trains an Isolation Forest model on normal traffic and flags rare flows as anomalies.
- 🧪 Simulated Attack Generator:** A custom Python script mimics abnormal behavior (e.g., port scans, floods) to test the system.
- 📊 Visualization:** Generates scatter plots (source vs. destination ports) showing normal vs anomalous flows.
- 📁 Output Logging:** Saves prediction results in a labeled CSV with anomaly flags (`1` = normal, `-1` = anomalous).

---

## 🛠️ Tech Stack

| Layer | Tools/Technologies |
|-------|---------------------|
| Language | Python 3 |
| Traffic Capture| Scapy |
| Data Processing | Pandas, ipaddress |
| Model | Isolation Forest (`scikit-learn`) |
| Visualization | Matplotlib, Seaborn |
| Attack Simulation| socket (custom script) |
| Environment | WSL2 (Ubuntu on Windows 10/11) |

---

## 🧪 How It Works

1. Run `five_tuple_logger.py` to capture live traffic.
2. (Optional) Run `simulate_abnormal_traffic.py` to inject fake malicious traffic.
3. Run `detect_anomalies.py` to:
   - Preprocess and encode traffic
   - Train an Isolation Forest model
   - Predict and label anomalies
   - Visualize results in `anomaly_plot.png`
4. Check the output in `five_tuple_with_anomaly.csv`.

---

## 📂 Output Files

- `five_tuple_with_anomaly.csv` — labeled traffic with anomaly predictions  
- `anomaly_plot.png` — scatter plot showing normal vs anomalous flows  
- (Optional) `five_tuple_log.csv` — raw captured data

---

## 📈 Sample Results

- Normal Packets:~90–95%  
- Anomalies Detected: ~5–10% (e.g., port 22/1900, rare destination IPs, high UDP bursts)  
- Graphical Output: Red X’s indicate anomalies, green dots indicate normal behavior

---

## 🧠 Learning Outcomes

> By using unsupervised learning (Isolation Forest), the system can detect network anomalies without needing labeled attack data or fixed rules — enabling flexible, adaptive security monitoring.

---

## ✅ Future Improvements

- Live dashboard using Streamlit or Flask  
- Real-time detection pipeline (e.g., with Kafka or sockets)  
- Integration with alerting/notification systems  
- Extension to deep packet inspection (DPI) for payload-based detection

---

## 📄 License

This project is for educational use. No license or commercial use implied.

---

