const express = require('express');
const axios = require('axios');  // For external API requests
const app = express();

const getProductInfo = (productName) => {
  // You can replace this with actual API calls or scraping
  return {
    product_name: productName,
    specifications: {
      color: 'Red',
      battery_life: '12 hours',
      dimensions: '10x8x6 inches',
      weight: '1.2 kg'
    },
    pricing: {
      price: 199.99,
      currency: 'USD',
      availability: 'In Stock'
    },
    manufacturer: {
      name: 'RoboTech Inc.',
      website: 'https://www.robotech.com'
    },
    reviews: [
      {
        user: 'John Doe',
        rating: 4.5,
        comment: 'Great robot! Does everything I need.'
      }
    ]
  };
};

app.get('/getProductInfo', (req, res) => {
  const productName = req.query.query;
  if (!productName) {
    return res.status(400).json({ error: 'Product name is required' });
  }
  
  const productData = getProductInfo(productName);
  res.json(productData);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
