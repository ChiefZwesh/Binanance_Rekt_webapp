# BinanceRekt - Liquidation Price Feed

BinanceRekt is a Django project that provides a real-time feed of Binance liquidations and displays them in a user-friendly dashboard. It also includes an embedded TradingView widget to track market data for a specific trading pair.

## Features

- Real-time Binance liquidation data feed
- User-friendly dashboard to display liquidations
- Embedded TradingView widget for market analysis
- Automatic refresh of the liquidation table every 5 seconds

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (3.7 or higher)
- Django (3.2 or higher)
- Binance WebSocket API (used for real-time liquidation data)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/BinanceRekt.git
cd BinanceRekt
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `stream.py` script to start the WebSocket connection and retrieve real-time liquidation data:

```bash
python stream.py
```

2. Set up your Django project by running migrations:

```bash
python manage.py migrate
```

3. Start the Django development server:

```bash
python manage.py runserver
```

4. Access the application in your web browser at http://localhost:8000/dashboard.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature/fix: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push the branch to your fork: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
*Disclaimer: This project is for educational and informational purposes only. Trading involves risk, and the content provided here does not constitute financial advice. Always do your research and consider seeking professional advice before making any investment decisions.*
