import streamlit as st
import pandas as pd
import numpy as np


# Sample Dataset
def create_sample_dataset():
    data = [
        {
            "Product": "Product A",
            "Category": "Medical",
            "Department": "IT",
            "Price": 1200,
        },
        {
            "Product": "Product B",
            "Category": "Medical",
            "Department": "Intensive Care",
            "Price": 800,
        },
        {
            "Product": "Product C",
            "Category": "Furniture",
            "Department": "Ortopedics",
            "Price": 350,
        },
        {
            "Product": "Product D",
            "Category": "Medical",
            "Department": "Audio",
            "Price": 250,
        },
        {
            "Product": "Product E",
            "Category": "Wearables",
            "Department": "Intensive Care",
            "Price": 300,
        },
        {
            "Product": "Product F",
            "Category": "Medical",
            "Department": "IT",
            "Price": 500,
        },
        {
            "Product": "Product G",
            "Category": "Furniture",
            "Department": "Ortopedics",
            "Price": 120,
        },
        {
            "Product": "Product H",
            "Category": "Medical",
            "Department": "Intensive Care",
            "Price": 400,
        },
    ]
    return pd.DataFrame(data)


# Gross Margin Calculation
def calculate_gross_margin(price, rebate_percentage, volume):
    """
    Calculate gross margin with volume-based discounts

    Discount Brackets:
    - Up to 10 products: 5% volume discount
    - Up to 20 products: 10% volume discount
    - Up to 50 products: 15% volume discount
    """
    # Rebate calculation
    rebate = price * rebate_percentage

    # Volume discount calculation
    volume_discount_percentage = 0
    if volume <= 10:
        volume_discount_percentage = 0.05
    elif volume <= 20:
        volume_discount_percentage = 0.10
    elif volume <= 50:
        volume_discount_percentage = 0.15

    volume_discount = price * volume_discount_percentage

    # Gross Margin calculation
    gross_margin = price - rebate - volume_discount

    return {
        "Price": int(price),
        "Rebate": int(-rebate),
        "Volume Discount": int(-volume_discount),
        "Gross Margin": int(gross_margin),
    }


# Streamlit Dashboard
def main():
    st.title("Gross Margin Simulation Dashboard")

    # Load sample dataset
    df = create_sample_dataset()

    # Sidebar for inputs
    st.sidebar.header("Simulation Parameters")

    # Product Selection
    product = st.sidebar.selectbox(
        "Select Product", df["Product"].unique(), key="product_select"
    )

    # Get selected product details
    selected_product = df[df["Product"] == product].iloc[0]

    # Rebate Percentage Selection
    rebate_percentage = (
        st.sidebar.slider(
            "Rebate Percentage",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            format="%d%%",
        )
        / 100.0
    )

    # Volume Selection
    volume = st.sidebar.number_input(
        "Volume", min_value=1, max_value=50, value=1, key="volume_input"
    )

    # Calculation
    margin_details = calculate_gross_margin(
        selected_product["Price"], rebate_percentage, volume
    )

    # Display Results
    st.header(f"Margin Simulation for {product}")

    # Details Table
    details_df = pd.DataFrame.from_dict(
        margin_details, orient="index", columns=["Value"]
    )
    details_df.index.name = "Metric"
    st.table(details_df)

    # Additional Product Information
    st.subheader("Product Details")
    st.write(f"**Category:** {selected_product['Category']}")
    st.write(f"**Department:** {selected_product['Department']}")


if __name__ == "__main__":
    main()
