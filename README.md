# samarth-rainfall-streamlit
Build For Bharat Fellowship demo app to visualize rainfall data from data.gov.in using Streamlit.

## 🔗 Live Demo
Check out the deployed application here: [https://samarth-rainfall-app-bjy4cwd7edpw63pvljipze.streamlit.app/](https://samarth-rainfall-app-bjy4cwd7edpw63pvljipze.streamlit.app/)

## 📁 How to Upload Your Code Files (Beginner-Friendly Guide)

### Method 1: Upload Files Directly on GitHub (Easiest for Beginners)
1. **Go to your repository**: Visit https://github.com/SurajAnalyzes/samarth-rainfall-streamlit
2. **Click "Add file"** button (top right, near the green "Code" button)
3. **Select "Upload files"**
4. **Drag and drop** your Python files, or click "choose your files" to browse
5. **Add a message** like "Add Streamlit app files" in the commit box
6. **Click "Commit changes"** button at the bottom

### Method 2: Using Git Commands (If you prefer command line)
```bash
# 1. Open terminal/command prompt on your computer
# 2. Navigate to your project folder
cd path/to/your/project

# 3. Initialize git (only needed once)
git init

# 4. Add all your files
git add .

# 5. Commit your files
git commit -m "Initial commit: Add rainfall visualization app"

# 6. Connect to GitHub repository
git remote add origin https://github.com/SurajAnalyzes/samarth-rainfall-streamlit.git

# 7. Push to GitHub
git branch -M main
git push -u origin main
```

## 📦 Project Structure (Recommended)
```
samarth-rainfall-streamlit/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/                 # Folder for data files (optional)
│   └── rainfall_data.csv
└── .gitignore           # Files to ignore (optional)
```

## 🚀 Getting Started

1. Clone this repository:
```bash
git clone https://github.com/SurajAnalyzes/samarth-rainfall-streamlit.git
cd samarth-rainfall-streamlit
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## 📋 requirements.txt Template
Create a file named `requirements.txt` with these contents:
```
streamlit
pandas
numpy
plotly
matplotlib
```

## 💡 Tips for Beginners
- **Commit often**: Save your changes frequently with meaningful messages
- **Use .gitignore**: Don't upload large data files or temporary files
- **README is important**: Keep this file updated with project info
- **Test locally first**: Make sure your app works on your computer before uploading

## 🎯 Project Description
This project is built as part of the Build For Bharat Fellowship. It visualizes rainfall data from data.gov.in using Streamlit, making it easy to explore and understand rainfall patterns across India.

## 📧 Contact
Maintained by: Suraj Kadam (SurajAnalyzes)

---
**Need Help?**
- GitHub Documentation: https://docs.github.com/
- Streamlit Documentation: https://docs.streamlit.io/
- Git Tutorial: https://git-scm.com/docs/gittutorial
