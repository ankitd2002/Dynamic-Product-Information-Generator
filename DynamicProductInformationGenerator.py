from fastapi import FastAPI, HTTPException  # Import FastAPI and exception handling
import random  # Used for generating dynamic values
from datetime import datetime, timedelta  # For handling dates and times
import uvicorn  # To run the FastAPI application

# Create a FastAPI application instance
app = FastAPI()

# Helper function to generate a dynamic JSON object
def generate_product_data(product_name: str):
    """
    Generates a detailed JSON object for the given product name.

    Approach:
    - Randomized certain values (e.g., price, reviews) to simulate a realistic dynamic response.
    - Incorporated fields like manufacturer info, specifications, pricing, reviews, and availability.

    Challenges:
    - Balancing between static and dynamic content to ensure the data looks realistic while maintaining consistency.
    - Simulating real-world product attributes (e.g., stock distribution, battery life).

    Strategies for Data Accuracy:
    - Used fixed logical ranges for attributes like price and stock count to ensure values remain plausible.
    - Incorporated mock reviews with meaningful comments.
    - Ensured dates (e.g., discount validity) are realistic by using timedelta.

    Args:
    - product_name (str): The name of the product to generate data for.

    Returns:
    - dict: A detailed JSON object containing product information.
    """
    return {
        "product": {
            "id": str(random.randint(10000, 99999)),  # Unique product ID (mocked)
            "name": product_name,  # Input product name
            "description": f"The {product_name} is a state-of-the-art product designed for excellence.",
            "category": "Electronics",
            "manufacturer": {
                "name": "Tech Innovators Inc.",  # Mock manufacturer name
                "address": {
                    "street": "789 Technology Blvd",
                    "city": "Tech City",
                    "state": "California",
                    "postalCode": "94025",
                    "country": "USA"
                },
                "contact": {
                    "phone": "+1-800-TECH-123",
                    "email": "support@techinnovators.com",
                    "website": "https://www.techinnovators.com"
                }
            },
            "specifications": {
                "dimensions": {
                    "width": "12 cm",
                    "height": "18 cm",
                    "depth": "5 cm"
                },
                "weight": "1.1 kg",
                "battery": {
                    "type": "Rechargeable lithium-ion",
                    "capacity": "2500mAh",
                    "chargingTime": "2 hours",
                    "batteryLife": "8 hours"
                },
                "features": [
                    "Wireless connectivity",
                    "AI-powered automation",
                    "Sleek and portable design",
                    "Eco-friendly materials"
                ]
            },
            "pricing": {
                "currency": "USD",
                "price": round(random.uniform(50, 300), 2),  # Random price in a realistic range
                "discount": {
                    "isAvailable": True,
                    "percentage": random.choice([5, 10, 15]),  # Random discount percentage
                    "validUntil": (datetime.now() + timedelta(days=random.randint(5, 20))).strftime("%Y-%m-%d")  # Discount expiry date
                }
            },
            "availability": {
                "inStock": True,
                "stockCount": random.randint(20, 100),  # Simulated stock count
                "warehouses": [
                    {"location": "San Francisco, CA", "stock": random.randint(10, 50)},
                    {"location": "Austin, TX", "stock": random.randint(10, 50)}
                ]
            },
            "reviews": [
                {
                    "user": "techlover",
                    "rating": random.randint(4, 5),  # High ratings for positive bias
                    "comment": f"The {product_name} is amazing and very reliable!",
                    "date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")  # Recent reviews
                },
                {
                    "user": "gadgetguru",
                    "rating": random.randint(3, 5),  # Balanced ratings
                    "comment": f"I loved the features of {product_name}, but the battery life could improve.",
                    "date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
                }
            ],
            "tags": ["smart device", "electronics", "AI", "innovative", "portable"],
            "relatedProducts": [
                {"id": "45678", "name": "SmartGadget Pro", "url": "https://www.example.com/products/45678"},
                {"id": "78901", "name": "EcoTech Device", "url": "https://www.example.com/products/78901"}
            ]
        }
    }

# API Endpoint: Generates product information
@app.get("/getProductInfo")
def get_product_info(product_name: str):
    """
    API endpoint to generate product information dynamically.

    Approach:
    - Validate the input query parameter (`product_name`).
    - Leverage the helper function to generate a dynamic JSON response.

    Challenges:
    - Ensure that the API provides meaningful error messages for missing or invalid parameters.
    - Maintain a consistent schema for the JSON response.

    Args:
    - product_name (str): Name of the product provided as a query parameter.

    Returns:
    - dict: A JSON object containing the product information.
    """
    if not product_name:
        # Raise an exception if the product name is missing
        raise HTTPException(status_code=400, detail="Product name is required as a query parameter.")

    # Generate product data using the helper function
    product_data = generate_product_data(product_name)
    return product_data

# Entry point: Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    """
    Starts the FastAPI application server. 

    Technical Decision:
    - Chose Uvicorn as the ASGI server for its performance and compatibility with FastAPI.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
