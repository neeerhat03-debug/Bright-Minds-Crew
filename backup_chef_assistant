from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
import streamlit as st
st.title("Nigeria Chef Assistant 🍳")
st.write("Enter the ingredients you have, and I'll suggest a Nigeria recipe for you.")

# --- GROUP ADDS THEIR INPUT FIELDS HERE ---
ingredients = st.text_area("Your ingredients are:")

if st.button("Suggest a Recipe"):
    if ingredients:
        # --- GROUP ADDS THEIR PROMPT HERE ---
        prompt = f"I have these ingredients: {ingredients}. Suggest a simple recipe."

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",messages=[
        {
            "role": "system",
            "content": """You are Mama Cooks, a warm and knowledgeable 
            Nigerian chef with expertise in cuisines from across Nigeria — 
            Yoruba, Igbo, Hausa, and Delta cooking traditions. 
            
            When given ingredients, you always:
            - Suggest a Nigerian dish first before any other cuisine
            - Use local ingredient names (e.g. tatashe not red bell pepper, 
              iru not locust beans)
            - Structure your response as: Dish Name, Ingredients with 
              quantities, Step-by-step method, Cooking time, and one 
              serving suggestion
            - Write in a warm, encouraging tone like a trusted friend 
              teaching you in their kitchen
            - If the ingredients don't suggest a clear Nigerian dish, 
              suggest the closest traditional equivalent"""
        },
        {"role": "user",
            "content": f"I have these ingredients: {ingredients}.\
            What Nigerian dish can I make?"
        }
    ]
)
        

        st.subheader("Here's your recipe.")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter some ingredients first.")
