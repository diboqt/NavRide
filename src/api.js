// src/api.js
import axios from 'axios';

// Create an Axios instance
const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Change this to match your back end URL
});

// Add a request interceptor to include the Authorization header
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');  // Retrieve token from local storage
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default api;
