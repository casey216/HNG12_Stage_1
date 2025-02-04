# Number Classification API

A simple Flask-based API that classifies numbers based on mathematical properties and provides fun facts using the Numbers API.

## 🚀 Features
- Check if a number is **prime**, **perfect**, or an **Armstrong number**.
- Identify if the number is **odd** or **even**.
- Calculate the **sum of its digits**.
- Retrieve an interesting **fun fact** about the number.

## 📡 API Endpoint
**GET** `/api/classify-number?number=<your_number>`

### Example Request
```bash
GET https://localhost:5000/api/classify-number?number=371
```

### Example Response (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
  "number": "alphabet",
  "error": true
}
```

## ⚙️ Setup Instructions
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/casey216/HNG12_Stage_1.git
   cd number-classification-api
   ```

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Locally:**  
   ```bash
   python api/app.py
   ```
