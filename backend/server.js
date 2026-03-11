const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Basit bir test rotası
app.get('/api/status', (req, res) => {
    res.json({ status: 'success', message: 'Akıllı Tarım Backend Çalışıyor!' });
});

// AI tahminleri için örnek bir rota (İleride Python servisine bağlanacak)
app.post('/api/predict', (req, res) => {
    // Burada Python AI servisine istek atılacak
    const mockPrediction = {
        sulamaGerekli: true,
        tahminiVerim: "Yüksek",
        hastalikRiski: "Düşük"
    };
    res.json(mockPrediction);
});

app.listen(PORT, () => {
    console.log(`Sunucu http://localhost:${PORT} portunda çalışıyor.`);
});
