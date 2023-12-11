psutil is a Python library that provides an interface for retrieving information on running processes and system utilization, such as CPU, memory, disks, network, and sensors. The name "psutil" is derived from "process and system utilities."
to run docker image we use

# ✨Let’s Start the Project ✨

## **Part 1: Deploying the Flask application locally**

### **Step 1: Clone the code**

Clone the code from the repository:

```
git clone <repository_url>
```

### **Step 2: Install dependencies**

The application uses the **`psutil`** and **`Flask`, Plotly libraries. Install them using pip:

```
pip3 install -r requirements.txt
```

### **Step 3: Run the application**

To run the application, navigate to the root directory of the project and execute the following command:

```
python3 app.py
```

This will start the Flask server on **`localhost:5000`**.

### Tests
__init__.py file was created so that our tests directory tests/ is treated as a python package and not a standalone script                                                                                         
