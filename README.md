# 🖼️ Interactive Image Processing Toolbox

A Streamlit web app with 10 classic image processing tools built using OpenCV and NumPy. This tool lets you interactively apply transformations, view side-by-side comparisons, and download the results.

## 🚀 Features

* Upload any image (JPG/PNG) and convert it to grayscale automatically
* Choose from 10 different image processing operations:

  1. Halftoning
  2. Reduce Intensity Levels
  3. Pixel Replication Zoom
  4. Bilinear Interpolation Zoom
  5. Arithmetic Operations (Add, Subtract, Multiply, Divide)
  6. Intensity Transformations (Log, Inverse, Gamma)
  7. Histogram Equalization
  8. Spatial Filtering (Mean, Gaussian, Median)
  9. Laplacian Enhancement
  10. Unsharp Masking
* See side-by-side comparison of original vs processed image
* Download the processed image

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/)
* [OpenCV (cv2)](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Pillow](https://python-pillow.org/)

## 📦 Installation

Make sure you have Python 3.8 or later installed.

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/image-processing-toolbox.git
cd image-processing-toolbox
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## 🌐 Deployment

You can deploy this to [Streamlit Cloud](https://streamlit.io/cloud) by pushing the repo to GitHub and linking it to Streamlit.

## 📁 Folder Structure

```
image-processing-toolbox/
├── app.py
├── requirements.txt
└── README.md
```

## 📷 Example Use Cases

* Teaching digital image processing
* Rapid prototyping of vision filters
* Visual learning for contrast, scaling, and transformation techniques

## 🙌 Contribution

Feel free to fork, extend, and make pull requests. Suggestions and improvements are always welcome!

---

Built with ❤️ using Python and Streamlit.
