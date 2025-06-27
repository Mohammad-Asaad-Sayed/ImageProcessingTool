import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

st.set_page_config(page_title="Image Processing Toolbox", layout="wide")
st.title("🖼️ Interactive Image Processing Toolbox")

# --- Image Upload ---
uploaded = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded:
    image = Image.open(uploaded).convert("L")  # convert to grayscale
    img_np = np.array(image)
    st.sidebar.image(image, caption="Uploaded Image", use_container_width=True)
else:
    st.warning("Upload an image to get started.")
    st.stop()

# --- Toolbox Selection ---
tool = st.sidebar.selectbox("Choose a Processing Tool", [
    "Halftoning",
    "Reduce Intensity Levels",
    "Pixel Replication Zoom",
    "Bilinear Interpolation Zoom",
    "Arithmetic Operations",
    "Intensity Transformations",
    "Histogram Equalization",
    "Spatial Filtering",
    "Laplacian Enhancement",
    "Unsharp Masking"
])

# Utility to generate download button
def download_button(image_array, filename):
    img_pil = Image.fromarray(image_array)
    buf = io.BytesIO()
    img_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button("Download Image", byte_im, file_name=filename, mime="image/png")

# Utility to show side-by-side comparison
def show_comparison(original, transformed, labels=("Original", "Transformed")):
    col1, col2 = st.columns(2)
    with col1:
        st.image(original, caption=labels[0], use_container_width=True)
    with col2:
        st.image(transformed, caption=labels[1], use_container_width=True)

# --- Halftoning ---
if tool == "Halftoning":
    st.header("Halftoning (Threshold Binarization)")
    threshold = st.slider("Threshold", 0, 255, 128)
    bin_img = (img_np > threshold) * 255
    bin_img = bin_img.astype(np.uint8)
    show_comparison(img_np, bin_img)
    download_button(bin_img, "halftoned.png")

# --- Reduce Intensity Levels ---
elif tool == "Reduce Intensity Levels":
    st.header("Reduce Intensity Levels")
    levels = st.slider("Number of Levels", 2, 256, 8)
    step = 256 // levels
    reduced = ((img_np // step) * step).astype(np.uint8)
    show_comparison(img_np, reduced)
    download_button(reduced, "reduced_intensity.png")

# --- Pixel Replication Zoom ---
elif tool == "Pixel Replication Zoom":
    st.header("Zoom / Shrink with Pixel Replication")
    scale = st.slider("Scale Factor", 0.1, 5.0, 2.0)
    resized = cv2.resize(img_np, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    show_comparison(img_np, resized)
    download_button(resized, "pixel_replication_zoom.png")

# --- Bilinear Interpolation Zoom ---
elif tool == "Bilinear Interpolation Zoom":
    st.header("Zoom / Shrink with Bilinear Interpolation")
    scale = st.slider("Scale Factor", 0.1, 5.0, 2.0)
    resized = cv2.resize(img_np, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    show_comparison(img_np, resized)
    download_button(resized, "bilinear_zoom.png")

# --- Arithmetic Operations ---
elif tool == "Arithmetic Operations":
    st.header("Arithmetic Operations")
    uploaded2 = st.file_uploader("Upload another image (same size)", type=["png", "jpg", "jpeg"], key="img2")
    if uploaded2:
        image2 = Image.open(uploaded2).convert("L")
        img_np2 = np.array(image2.resize(image.size))
        operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
        if operation == "Add":
            result = cv2.add(img_np, img_np2)
        elif operation == "Subtract":
            result = cv2.subtract(img_np, img_np2)
        elif operation == "Multiply":
            result = cv2.multiply(img_np, img_np2)
        elif operation == "Divide":
            result = cv2.divide(img_np, img_np2)
        show_comparison(img_np2, result, labels=("Second Image", f"Result of {operation}"))
        download_button(result, f"arithmetic_{operation.lower()}.png")
    else:
        st.info("Upload a second image for arithmetic operations.")

# --- Intensity Transformations ---
elif tool == "Intensity Transformations":
    st.header("Intensity Transformations")
    mode = st.selectbox("Transformation Type", ["Log", "Inverse", "Gamma"])
    if mode == "Log":
        c = 255 / np.log(1 + np.max(img_np))
        result = c * np.log(1 + img_np)
    elif mode == "Inverse":
        result = 255 - img_np
    elif mode == "Gamma":
        gamma = st.slider("Gamma Value", 0.1, 5.0, 1.0)
        norm_img = img_np / 255.0
        result = np.power(norm_img, gamma) * 255
    result = result.astype(np.uint8)
    show_comparison(img_np, result)
    download_button(result, f"intensity_{mode.lower()}.png")

# --- Histogram Equalization ---
elif tool == "Histogram Equalization":
    st.header("Histogram Equalization")
    result = cv2.equalizeHist(img_np)
    show_comparison(img_np, result)
    download_button(result, "histogram_equalized.png")

# --- Spatial Filtering ---
elif tool == "Spatial Filtering":
    st.header("Spatial Filtering")
    filter_type = st.selectbox("Filter Type", ["Mean", "Gaussian", "Median"])
    ksize = st.slider("Kernel Size", 3, 15, 3, step=2)
    if filter_type == "Mean":
        result = cv2.blur(img_np, (ksize, ksize))
    elif filter_type == "Gaussian":
        result = cv2.GaussianBlur(img_np, (ksize, ksize), 0)
    elif filter_type == "Median":
        result = cv2.medianBlur(img_np, ksize)
    show_comparison(img_np, result)
    download_button(result, f"{filter_type.lower()}_filtered.png")

# --- Laplacian Enhancement ---
elif tool == "Laplacian Enhancement":
    st.header("Laplacian Enhancement")
    lap = cv2.Laplacian(img_np, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    show_comparison(img_np, lap)
    download_button(lap, "laplacian.png")

# --- Unsharp Masking ---
elif tool == "Unsharp Masking":
    st.header("Unsharp Masking")
    blur = cv2.GaussianBlur(img_np, (5, 5), 0)
    unsharp = cv2.addWeighted(img_np, 1.5, blur, -0.5, 0)
    show_comparison(img_np, unsharp)
    download_button(unsharp, "unsharp_mask.png")
