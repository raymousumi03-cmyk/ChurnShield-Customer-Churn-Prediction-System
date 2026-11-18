

import streamlit as st
import pandas as pd
import joblib

# ============================================================
# 1. PAGE SETUP
# ============================================================
st.set_page_config(
    page_title="ChurnShield",
    page_icon="🛡️",
    layout="wide"
)

# ============================================================
# 2. PAGE DESIGN AND STYLING
# ============================================================
st.markdown("""
<style>
/* Main page */
.stApp {
    background: #f7fee7 !important;
    color: #000000 !important;
    font-family: Arial, sans-serif;
}

.block-container {
    max-width: 1350px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* All headings and labels in black */
h1, h2, h3, h4, p,
label, .stMarkdown, .stCaption,
[data-testid="stWidgetLabel"],
[data-testid="stMarkdownContainer"] {
    color: #000000 !important;
}

/* Center and enlarge ChurnShield banner */
.hero {
    background: linear-gradient(120deg, #fde047, #a3e635, #22c55e);
    padding: 38px 20px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 30px;
    border: 2px solid #65a30d;
    box-shadow: 0 8px 24px rgba(34, 197, 94, 0.30);
}

.hero h1 {
    color: #000000 !important;
    font-size: 3.2rem !important;
    font-weight: 900 !important;
    margin: 0 0 12px 0;
    text-align: center;
}

.hero p {
    color: #000000 !important;
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    text-align: center;
    margin: 6px 0;
}

/* Section headings */
h2, h3 {
    font-weight: 800 !important;
}

.stSelectbox label,
.stNumberInput label,
.stSlider label {
    color: #000000 !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
}

/* Dropdown box */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 2px solid #65a30d !important;
    border-radius: 9px !important;
    min-height: 43px !important;
}

/* Selected dropdown value: force BLACK */
div[data-baseweb="select"] span,
div[data-baseweb="select"] div,
div[data-baseweb="select"] input,
div[data-baseweb="select"] [role="combobox"] {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    opacity: 1 !important;
}

/* Dropdown menu and options */
div[data-baseweb="popover"],
div[data-baseweb="menu"],
div[data-baseweb="popover"] ul {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] li,
div[data-baseweb="popover"] li span,
div[data-baseweb="menu"] li,
[role="option"] {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] li:hover,
[role="option"]:hover {
    background-color: #dcfce7 !important;
}

/* Number input boxes */
.stNumberInput input,
input[type="number"],
.stTextInput input,
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    caret-color: #000000 !important;
    opacity: 1 !important;
    border-radius: 8px !important;
}

/* Number input buttons */
.stNumberInput button {
    background-color: #dcfce7 !important;
    color: #000000 !important;
    border: 1px solid #65a30d !important;
}

/* Input box borders */
[data-testid="stNumberInput"] div[data-baseweb="input"],
[data-testid="stTextInput"] div[data-baseweb="input"] {
    background-color: #ffffff !important;
    border: 2px solid #65a30d !important;
    border-radius: 9px !important;
}

/* Slider */
[data-testid="stSlider"] {
    color: #000000 !important;
}

[data-testid="stSlider"] [role="slider"] {
    background-color: #16a34a !important;
    border-color: #15803d !important;
}

/* Prediction button */
.stButton button {
    background: linear-gradient(90deg, #65a30d, #16a34a) !important;
    color: #000000 !important;
    border: 2px solid #166534 !important;
    border-radius: 10px !important;
    min-height: 50px !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
}

.stButton button p,
.stButton button span {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

.stButton button:hover {
    background: #a3e635 !important;
    border-color: #166534 !important;
}

/* Results */
[data-testid="stMetricValue"] {
    color: #000000 !important;
    font-weight: 800 !important;
}

[data-testid="stAlert"] {
    border-radius: 10px;
}

hr {
    border-color: #84cc16 !important;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 25px 12px;
    }

    .hero h1 {
        font-size: 2.2rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. LOAD TRAINED MODEL
# ============================================================
model = joblib.load("final_gb_classifier.pkl")

# ============================================================
# 4. CENTERED CHURNSHIELD HEADING
# ============================================================
st.markdown("""
<div class="hero">
    <h1>🛡️ ChurnShield</h1>
    <p>Customer Churn Prediction System</p>
    <p>Predict customer churn and identify retention opportunities.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 5. CUSTOMER PROFILE
# ============================================================
st.subheader("👤 Customer Profile")

c1, c2, c3 = st.columns(3)

with c1:
    gender = st.selectbox(
        "Gender", [0, 1],
        format_func=lambda x: {0: "Female", 1: "Male"}[x]
    )
    senior_citizen = st.selectbox(
        "Senior Citizen", [0, 1],
        format_func=lambda x: {0: "No", 1: "Yes"}[x]
    )

with c2:
    partner = st.selectbox(
        "Partner", [0, 1],
        format_func=lambda x: {0: "No", 1: "Yes"}[x]
    )
    dependents = st.selectbox(
        "Dependents", [0, 1],
        format_func=lambda x: {0: "No", 1: "Yes"}[x]
    )

with c3:
    phone_service = st.selectbox(
        "Phone Service", [0, 1],
        format_func=lambda x: {0: "No", 1: "Yes"}[x]
    )
    multiple_lines = st.selectbox(
        "Multiple Lines", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No phone service"
        }[x]
    )

# ============================================================
# 6. INTERNET AND ADDITIONAL SERVICES
# ============================================================
st.markdown("---")
st.subheader("🛠️ Internet and Additional Services")

c1, c2, c3 = st.columns(3)

with c1:
    internet_service = st.selectbox(
        "Internet Service", ["DSL", "Fiber optic", "No"]
    )
    online_security = st.selectbox(
        "Online Security", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )
    online_backup = st.selectbox(
        "Online Backup", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )

with c2:
    device_protection = st.selectbox(
        "Device Protection", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )
    tech_support = st.selectbox(
        "Tech Support", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )

with c3:
    streaming_tv = st.selectbox(
        "Streaming TV", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )
    streaming_movies = st.selectbox(
        "Streaming Movies", [0, 1, 2],
        format_func=lambda x: {
            0: "No", 1: "Yes", 2: "No internet service"
        }[x]
    )

# ============================================================
# 7. CONTRACT AND BILLING
# ============================================================
st.markdown("---")
st.subheader("💳 Contract and Billing")

c1, c2, c3 = st.columns(3)

with c1:
    contract = st.selectbox(
        "Contract", ["Month-to-month", "One year", "Two year"]
    )
    paperless_billing = st.selectbox(
        "Paperless Billing", [0, 1],
        format_func=lambda x: {0: "No", 1: "Yes"}[x]
    )

with c2:
    monthly_charges = st.slider(
        "Monthly Charges",
        min_value=0.0,
        value=500.0,
        step=1.0,
        format="%.2f"
    )
    total_charges = st.slider(
        "Total Charges",
        min_value=0.0,
        value=5000.0,
        step=10.0,
        format="%.2f"
    )

with c3:
    tenure = st.slider(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

# ============================================================
# 8. PREDICT CHURN
# ============================================================
st.markdown("---")

if st.button("🔮 Predict Churn Risk", use_container_width=True):

    data = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": {
            "DSL": 0, "Fiber optic": 1, "No": 2
        }[internet_service],
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": {
            "Month-to-month": 0, "One year": 1, "Two year": 2
        }[contract],
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": {
            "Electronic check": 0,
            "Mailed check": 1,
            "Bank transfer (automatic)": 2,
            "Credit card (automatic)": 3
        }[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "tenure": tenure
    }])

    # Match the model's expected column order
    data = data.reindex(columns=model.feature_names_in_)

    if data.isnull().any().any():
        st.error(
            "Some model features are missing. "
            "Please check your training columns."
        )
    else:
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]

        st.subheader("📊 Prediction Result")
        st.metric("Churn Probability", f"{probability:.1%}")

        if prediction == 1:
            st.error(
                "⚠️ This customer is likely to churn. "
                "Consider offering support or a retention plan."
            )
        else:
            st.success(
                "✅ This customer is likely to stay."
            )