# 🖋️ Digit Recognition System

![Project Banner](assets/banner.png)

A professional, high-performance web application designed to recognize handwritten digits in real-time. Built with **Django** and powered by a **Deep Learning model** trained on the MNIST dataset, this system provides an intuitive interface for digit classification from images.

---

## 🚀 Key Features

- **Real-time Recognition**: Upload or capture an image of a handwritten digit (0-9) and get instant predictions.
- **Deep Learning Core**: Utilizes a Convolutional Neural Network (CNN) trained on thousands of MNIST samples for high accuracy.
- **Responsive Web UI**: A sleek, dark-themed interface optimized for both desktop and mobile devices.
- **Image Preprocessing**: Automatic scaling, grayscale conversion, and normalization of uploaded images to match model input requirements.
- **Secure Integration**: Implements Django's CSRF protection for secure image submission.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Django 4.2+, Python 3.x |
| **Deep Learning** | Keras, TensorFlow |
| **Image Processing** | Pillow (PIL), NumPy |
| **Frontend** | HTML5, Vanilla CSS, JavaScript (Fetch API) |
| **Production Server** | Gunicorn (configured in Procfile) |

---

## 📂 Project Structure

```text
DigitRecognitionSystem/
├── assets/                     # Media and documentation resources
├── handwritingrecognizer/      # Project configuration and settings
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main routing
│   └── wsgi.py/asgi.py         # Entry points
├── recognizer/                 # Core application logic
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   └── index.html          # Main User Interface
│   ├── views.py                # Prediction and routing logic
│   ├── mnist_model.keras       # Pre-trained CNN model
│   └── urls.py                 # App-specific routes
├── manage.py                   # Django management script
├── requirements.txt            # Project dependencies
└── Procfile                    # Deployment configuration
```

---

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sourabh7singh/DigitRecognitionSystem.git
cd DigitRecognitionSystem
```

### 2. Set Up Virtual Environment
```bash
python -m venv env
# Windows
.\env\Scripts\activate
# Linux/macOS
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

---

## 🏁 Usage

1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
2. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.
3. **Recognize Digits**:
   - Click "Choose File" or take a photo of a handwritten digit.
   - Click the **Recognize Digit** button.
   - The system will process the image and display the predicted digit in an alert.

---

## 🧠 Model Details

The underlying model is a Convolutional Neural Network (CNN) optimized for the MNIST dataset.
- **Input Shape**: 28x28 grayscale image.
- **Architecture**: Multiple convolution and pooling layers followed by dense layers.
- **Training**: Trained on 60,000 samples with a validation set for maximum performance.

---

## 🧪 Future Enhancements
- [ ] **Canvas Drawing**: Add an interactive canvas to draw digits directly on the screen.
- [ ] **Multi-Digit Support**: Ability to recognize multiple digits in a single image.
- [ ] **Advanced Visualization**: Show the model's confidence scores for each digit.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
**Developed by [Sourabh Singh](https://github.com/Sourabh7singh)**
