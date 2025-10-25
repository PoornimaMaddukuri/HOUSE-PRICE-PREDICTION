# 🏠 Smart House Price Predictor

A **Machine Learning + Streamlit** web app that predicts **house prices** based on user inputs like area type, number of bedrooms, and total area in square feet.

---

## 📘 Project Overview

This project demonstrates how to use a **Linear Regression** model to predict real-estate prices.  
It provides an **interactive Streamlit UI** where users can input property details and get an **instant estimated price**.

---

## 🚀 Features

✅ Predicts house price using **Linear Regression**  
✅ Encodes categorical data (`Urban` / `Rural`) using **LabelEncoder**  
✅ Clean, interactive **Streamlit interface**  
✅ Responsive input fields and styled output display  

---

## 📂 Project Structure

```
📁 Smart-House-Price-Predictor
├── app.py               # Main Streamlit app
├── house.csv            # Dataset used for model training
├── HOUSE.ipynb          # Jupyter notebook for data exploration/training
└── README.md            # Project documentation
```

---

## 🧠 Tech Stack

- **Python 3.10+**  
- **Streamlit** – for building the interactive web app  
- **Pandas** – for data handling  
- **NumPy** – for numerical computations  
- **Scikit-learn** – for model training and encoding  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Smart-House-Price-Predictor.git
cd Smart-House-Price-Predictor
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can create one using:
```bash
pip freeze > requirements.txt
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📊 Dataset Details

The dataset (`house.csv`) contains the following columns:
| Column Name | Description |
|--------------|-------------|
| area_type | Type of area (Urban / Rural) |
| bedrooms | Number of bedrooms |
| area_sqft | Total built-up area in square feet |
| price | Target variable (House price in ₹) |

---

## 💡 How It Works

1. The model is trained using **Linear Regression** on the dataset.  
2. The app takes user input (area type, bedrooms, area size).  
3. These values are preprocessed (encoding, scaling).  
4. The trained model predicts the **estimated house price** instantly.  

---

## 🖼️ Example Output

When the user enters:
- Area Type: Urban  
- Bedrooms: 3  
- Area (sq ft): 1500  

The model may output something like:
> 💰 **Estimated House Price: ₹45,00,000**

---

## 🤝 Contributing

Contributions are always welcome!  
If you’d like to improve the UI, model, or dataset, feel free to fork this repo and open a pull request.

---

## 🧾 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.

---

## 👩‍💻 Author

**Poornima Maddukuri**  
*Machine Learning & Data Science Enthusiast*  
📫 [GitHub Profile](https://github.com/<your-username>)
