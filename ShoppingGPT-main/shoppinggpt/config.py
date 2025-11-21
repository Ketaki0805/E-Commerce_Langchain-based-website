# config.py
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv(r"C:\Users\DELL\PycharmProjects\GPT_Project\ShoppingGPT-main\shoppinggpt\.env")

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Paths
DATA_PRODUCT_PATH = r"C:\Users\DELL\PycharmProjects\GPT_Project\ShoppingGPT-main\data\products.db"
DATA_TEXT_PATH = r"C:\Users\DELL\PycharmProjects\GPT_Project\ShoppingGPT-main\data\policy.txt"
STORE_DIRECTORY = r"C:\Users\DELL\PycharmProjects\GPT_Project\ShoppingGPT-main\data\datastore"

# Embeddings
load_dotenv(r"C:\Users\DELL\PycharmProjects\GPT_Project\ShoppingGPT-main\shoppinggpt\.env")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDINGS = GoogleGenerativeAIEmbeddings(model="models/embedding-001")