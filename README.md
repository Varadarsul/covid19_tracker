# 🌍 COVID-19 Global Dashboard

A visually enhanced Flask web application that displays real-time COVID-19 statistics per country using data from the [disease.sh](https://disease.sh/) API. The project includes individual country views with maps, heatmaps, and forecasted case trends using data analysis techniques.

## 🔧 Features

- 🌐 Real-time data from [disease.sh API](https://disease.sh)
- 📊 Country-wise stats (cases, deaths, recoveries)
- 🗺️ Interactive map with heatmap for individual countries
- 📈 7-day forecast for selected countries using linear regression
- 🎨 Modern, responsive UI with gradient background and styled tables

## 📁 Project Structure

```

covid\_dashboard/
├── app.py
├── requirements.txt
├── covid\_data/
│   └── world\_data.csv (optional)
├── data\_analysis/
│   └── forecast.py
├── templates/
│   ├── index.html
│   └── country.html
├── static/
│   ├── style.css
│   └── charts.js

````

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Varadarsul/covid19_tracker.git
cd covid19_tracker
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
python app.py
```

Open your browser and go to:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## 📊 Forecasting (Optional)

To run the 7-day forecast chart:

```bash
python data_analysis/forecast.py
```

This script fetches recent historical data for a selected country (default: India), applies linear regression, and plots future trends.

## 📸 Screenshots
### 🏠 Homepage
![Homepage](https://github.com/Varadarsul/covid19_tracker/blob/main/screenshots/Screenshot%202025-05-04%20175426.png?raw=true)

### 🌍 Country Page
![Country Page](assets/country_page.png)

## 📡 Data Source

This application uses the public [disease.sh](https://disease.sh/docs/#/) API which aggregates data from trusted sources like WHO, CDC, and Johns Hopkins University.

## 📃 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change or add.

## ✨ Credits

* [disease.sh API](https://disease.sh/)
* [Flask](https://flask.palletsprojects.com/)
* [Chart.js](https://www.chartjs.org/)
* [Leaflet.js](https://leafletjs.com/)

```

