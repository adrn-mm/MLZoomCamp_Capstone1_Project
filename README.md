# Project Description

## Problem Statement
The telecom industry is growing rapidly due to consumers' increasing reliance on internet communication. This has created intense competition among telecom companies and ISPs, giving customers more choice. Customer Churn occurs when customers switch providers, leading to a decrease in revenue for the original provider. To address this, telecom companies must understand the drivers of Customer Churn, improve service quality, offer competitive pricing, and provide additional benefits to retain customers. Addressing Customer Churn is crucial for maintaining a competitive advantage and success in the telecom industry.
![](https://www.ibef.org/assets/images/Telecom-Industry-2.jpg)

## Proposed Solution
In response to the challenge of predicting customer churn in the telecom industry, a proposed machine learning solution aims to analyze customer behavior and patterns, helping telecom companies proactively identify potential churn and take preventive measures. This predictive approach is crucial for maintaining competitiveness in the rapidly evolving telecom sector.

# Download Dataset
The data is already provided in this repo, but you can download it using this command:
- training data:
```bash
wget -O data/customer_churn_train.csv https://raw.githubusercontent.com/adrn-mm/MLZoomCamp_Capstone1_Project/master/data/customer_churn_train.csv
```
- testing data:
```bash
wget -O data/customer_churn_test.csv https://raw.githubusercontent.com/adrn-mm/MLZoomCamp_Capstone1_Project/master/data/customer_churn_test.csv
```

# Depedency & Environment Management
### Activate Virtual Environment & Install Dependencies
1. Activate the virtual environment using the appropriate command for your operating system:
 - **Windows**
```
.venv\Scripts\activate
```
   - **MacOS and Linux**
```
source .venv/bin/activate
```
2. Upgrade PIP first using this command
```
python -m pip install --upgrade pip
``` 
3. Install packages using requirements.txt
```
pip install -r requirements.txt
```
4. Deactivate the virtual environment (optional)
```
deactivate
```
### Python Version Using in This Project
Python 3.10.11

# Containerization
Here are the steps and commands to create a Docker image and run a Docker container:
1. Open Terminal: First, you need to open a terminal on your machine.
2. Navigate to Your Project Directory: Use the cd command to navigate to the directory containing your project files.
```bash
cd .\source\
```
3. Build the Docker Image: You will use the docker build command to create an image. Replace your_image_name with the name you want to give your Docker image.
```bash
docker build -t your_image_name .
```
4. Check the Image: After building the image, you can see it listed by running:
```bash
docker images
```
5. Run the Docker Container: Now you can run a container from the image you just built. Replace your_container_name with the name you want to give your Docker container. Also, if your application needs specific ports to be open or environment variables, make sure to specify those with the -p and -e flags respectively.
```bash
docker run --name your_container_name -p 8080:8080 -d your_image_name
```

# Project Structure


# Project Evaluation Criteria
- [x] Problem Description
- [x] EDA
- [x] Model Training
- [x] Exporting to Script
- [x] Reproducibility
- [x] Model Deployment
- [x] Dependency and environment management
- [x] Containerization
- [ ] Cloud Deployment