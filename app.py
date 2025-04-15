import streamlit as st
import numpy as np
import pickle
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY") 

# Load model and transformer
with open('final_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('transformer.pkl', 'rb') as file:
    pt = pickle.load(file)


# Gemini Suggestions Function
def gemini_suggestions_via_api(pred, input_features):
    prompt = f"""
    A person has a {'high' if pred > 0.5 else 'low'} risk of cardiovascular disease.
    Based on the following lifestyle and health inputs:

    {input_features}

    Please provide clear, empathetic suggestions in English and Hindi that cover:
    - Mental well-being
    - Physical health
    - Behavioral improvement
    - Emotional support

    Tone should be calming and motivational, especially if risk is high.
    """

    try:
        gemini_model = genai.GenerativeModel('gemini-pro')
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {e}"


# Prediction Logic
def prediction(input_list):
    input_list = np.array(input_list, dtype=object)
    pred = model.predict_proba([input_list])[:, 1][0]

    if pred > 0.5:
        result = f'''⚠️ You Have More Chances of Getting Diseased  
Your Probability Of Having Cardiovascular Disease is {round(pred, 2)}  
Take Care!'''
        st.error(result)
    else:
        result = f'''✅ You Have Less Chances of Getting Diseased  
Your Probability Of Having Cardiovascular Disease is {round(pred, 2)}  
Stay Healthy!'''
        st.success(result)
    return pred, result


# Main App
def main():
    st.set_page_config(page_title="CardioLens", layout="centered")
    st.title('💓 CardioLens: Lifestyle Data Based Heart Disease Risk Predictor')

    h = st.number_input('Enter Height (cm):', min_value=50, max_value=300, step=1)
    w = st.number_input('Enter Weight (kg):', min_value=1, max_value=200, step=1)
    gh = (lambda x: 0 if x == 'Poor' else 1 if x == 'Fair' else 2 if x == 'Good' else 3 if x == 'Very Good' else 4)(
        st.selectbox('What About Your General Health ?', ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']))
    bg = (lambda x: 0 if x == 'O' else 1 if x == 'B' else 2)(st.selectbox('What is Your Blood Group ?', ['A', 'B', 'O', 'AB']))
    age = (lambda x: 0 if x < 30 else 1 if x < 50 else 2)(st.slider('Tell us How old are you ? ', min_value=18, max_value=100, step=1))
    bmi = w / ((h / 100) ** 2)
    ckup = (lambda x: 0 if x == 'Never' else 1 if x == 'Within the past year' else 2 if x == 'Within the past 2 years' else 3 if x == 'Within the past 5 years' else 4)(
        st.selectbox("When was the last time you had a check-up?", ['Never', 'Within the past year', 'Within the past 2 years', 'Within the past 5 years']))
    smk = (lambda x: 0 if x == 'No' else 1)(st.selectbox('Do You Smoke ?', ['Yes', "No"]))
    sex = (lambda x: 0 if x == 'Female' else 1)(st.selectbox('Tell Us About Your Gender ?', ['Male', "Female"]))
    dp = (lambda x: 0 if x == 'Non Veg' else 1)(st.selectbox('Tell Us About Your Diet Preference ?', ['Veg', "Non Veg"]))
    gv = st.slider('Rate Your Green Vegetable Consumption (1 = low, 4 = high)', min_value=1, max_value=4, step=1)
    fr = st.slider('Rate Your Fruit Consumption (1 = low, 4 = high)', min_value=1, max_value=4, step=1)
    fry = st.slider('Rate Your Fried Food Consumption (1 = low, 4 = high)', min_value=1, max_value=4, step=1)
    alco = st.slider('Rate Your Alcohol Consumption (1 = low, 4 = high)', min_value=1, max_value=4, step=1)
    dep = (lambda x: 0 if x == 'No' else 1)(st.selectbox('Are You Feeling Depressed ?', ['Yes', "No"]))
    mar = (lambda x: 0 if x == 'Married' else 1)(st.selectbox('What About Your Marital Status ?', ['Married', "UnMarried"]))
    exer = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Do you work out every day?", ['Yes', "No"]))
    skin = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Have You Ever Diagnosed With Skin Cancer ?", ['Yes', "No"]))
    other = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Have You Ever Diagnosed With Any Type Of Cancer?", ['Yes', "No"]))
    arth = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Are You Suffering from Arthritis ?", ['Yes', "No"]))
    diab = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Do You Have Any Type Of Diabetes?", ['Yes', "No"]))
    vac = (lambda x: 0 if x == 'No' else 1)(st.selectbox("Are You Vaccinated Against Cardiovascular Disease ?", ['Yes', "No"]))

    tran_data = pt.transform([[h, w, bmi]])
    h_t, w_t, bmi_t = tran_data[0]

    input_list = [h_t, w_t, gh, bg, age, bmi_t, ckup, smk, sex, dp, gv, fr, fry, alco,
                  dep, mar, exer, skin, other, arth, diab, vac]

    input_data_summary = {
        "Height (cm)": h, "Weight (kg)": w, "BMI": round(bmi, 2), "General Health": gh,
        "Blood Group": bg, "Age Category": age, "Last Check-up": ckup,
        "Smoker": smk, "Gender": sex, "Diet": dp, "Green Veg": gv,
        "Fruits": fr, "Fried Food": fry, "Alcohol": alco, "Depressed": dep,
        "Married": mar, "Exercises": exer, "Skin Cancer": skin,
        "Other Cancer": other, "Arthritis": arth, "Diabetes": diab, "Vaccinated": vac
    }

    if st.button('Show Prediction'):
        pred, result_msg = prediction(input_list)
        suggestions = gemini_suggestions_via_api(pred, input_data_summary)
        st.markdown("### 🌟 Gemini AI Suggestions")
        st.markdown(suggestions)


if __name__ == '__main__':
    main()
