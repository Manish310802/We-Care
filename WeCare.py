import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained models (replace with your actual model files)
with open("Imodel3(70%).pickle", "rb") as file:
    model1 = pickle.load(file)

with open("Wmodel2(77%).pickle", "rb") as file:
    model2 = pickle.load(file)

# Set up the sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Model", ["PCOS Predictor (Infertility)", "PCOS Predictor (Fertility)"])

# Function for the first model
def model_1_interface():
    st.title("WE CARE - PCOS Predictor")
    st.header("Enter the biomarker values")

    # Input fields for the features of model 1
    beta_hcg_1 = st.number_input("Beta-HCG (I) (mIU/mL)", value=0.0)
    beta_hcg_2 = st.number_input("Beta-HCG (II) (mIU/mL)", value=0.0)
    amh = st.number_input("AMH (ng/mL)", value=0.0)

    # Button to predict
    if st.button("Predict"):
        # Prepare the input data for prediction
        input_data = pd.DataFrame([[beta_hcg_1, beta_hcg_2, amh]], 
                                  columns=["Beta_HCG_I", "Beta_HCG_II", "AMH"])
        
        # Make prediction
        prediction = model1.predict(input_data)
        
        # Display the result
        if prediction[0] == 1:  # Assuming 1 means PCOS detected
            st.success("*PCOS Detected*")
        else:
            st.success("*No PCOS Detected*")

# Function for the second model
def model_2_interface():
    st.title("WE CARE - PCOS Predictor")
    st.header("Enter the biomarker values")

    # Input fields for the features of model 2
    age = st.number_input("Age (yrs)", value=0, min_value=0)
    weight = st.number_input("Weight (Kg)", value=0.0, min_value=0.0)
    height = st.number_input("Height (Cm)", value=0.0, min_value=0.0)
    bmi = st.number_input("BMI", value=0.0)
    fsh = st.number_input("FSH (mIU/mL)", value=0.0)
    lh = st.number_input("LH (mIU/mL)", value=0.0)
    fsh_lh_ratio = st.number_input("FSH/LH", value=0.0)
    prl = st.number_input("PRL (ng/mL)", value=0.0)
    tsh = st.number_input("TSH (mIU/L)", value=0.0)
    vit_d3 = st.number_input("Vit D3 (ng/mL)", value=0.0)
    waist_hip_ratio = st.number_input("Waist:Hip Ratio", value=0.0)
    
    # Follicle numbers and average follicle sizes
    follicle_no_l = st.number_input("Follicle No. (L)", value=0)
    follicle_no_r = st.number_input("Follicle No. (R)", value=0)
    avg_f_size_l = st.number_input("Avg. F Size (L) (mm)", value=0.0)
    avg_f_size_r = st.number_input("Avg. F Size (R) (mm)", value=0.0)
    endometrium = st.number_input("Endometrium (mm)", value=0.0)

    # Button to predict
    if st.button("Predict"):
        # Prepare the input data for prediction
        input_data = pd.DataFrame([[age, weight, height, bmi, fsh, lh, fsh_lh_ratio, 
                                     prl, tsh, vit_d3, waist_hip_ratio,
                                     follicle_no_l, follicle_no_r, avg_f_size_l, 
                                     avg_f_size_r, endometrium]],
                                   columns=['Age (yrs)', 'Weight (Kg)', 'Height(Cm)',
                                            'BMI', 'FSH(mIU/mL)', 'LH(mIU/mL)',
                                            'FSH/LH', 'PRL(ng/mL)', 'TSH (mIU/L)', 
                                            'Vit D3 (ng/mL)', 'Waist:Hip Ratio', 'Follicle No. (L)', 
                                            'Follicle No. (R)', 'Avg. F size (L) (mm)', 
                                            'Avg. F size (R) (mm)', 'Endometrium (mm)'])
        
        # Make prediction
        prediction = model2.predict(input_data)
        
        # Display the result
        if prediction[0] == 1:  # Assuming 1 means PCOS detected
            st.success("*PCOS Detected*")
        else:
            st.success("*No PCOS Detected*")

# Display the corresponding model interface based on selection
if page == "PCOS Predictor (Infertility)":
    model_1_interface()
else:
    model_2_interface()

