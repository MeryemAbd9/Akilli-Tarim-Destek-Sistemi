from flask import Flask, request, jsonify
# import joblib  # İleride eğitilmiş modeli yüklemek için kullanılacak
# import pandas as pd

app = Flask(__name__)

# Örnek Model Yükleme (Şimdilik yorum satırı)
# model = joblib.load('tarim_modeli.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Gelen veriyi (sıcaklık, nem, toprak yapısı vb.) alıp modele sokacağız
        print("Gelen veri:", data)
        
        # mock_prediction = model.predict(pd.DataFrame([data]))
        
        # Şimdilik sahte (mock) veri dönüyoruz
        mock_result = {
            "prediction": "Sulama yapılması önerilir.",
            "confidence": 0.85
        }
        
        return jsonify(mock_result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # AI servisi 5000 portunda çalışacak
    app.run(port=5000, debug=True)
