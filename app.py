import streamlit as st
import pickle
import preprocessing   # IMPORTANT

# Load pipeline
with open("sentiment_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📝 Review Sentiment Analyzer")

review = st.text_area("Enter your review")

if st.button("Predict"):
    if review.strip() != "":
        prediction = model.predict([review])[0]
        probability = model.predict_proba([review])[0]

        if prediction == 1:
            st.success("Positive Review 😊")
            st.write(f"Confidence: {round(max(probability)*100,2)}%")
        else:
            st.error("Negative Review 😞")
            st.write(f"Confidence: {round(max(probability)*100,2)}%")
    else:
        st.warning("Please enter a review.")



# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        right: 20px;
        bottom: 10px;
        font-size: 13px;
        color: gray;
    }
    .footer a {
        text-decoration: none;
        color: gray;
    }
    </style>
    <div class="footer">
        Created by Sowmya kona | Hosted by 
        <a href="https://streamlit.io" target="_blank">Streamlit</a>
    </div>
    """,
    unsafe_allow_html=True
)