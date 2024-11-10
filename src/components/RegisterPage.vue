<template>
    <div class="register-container">
      <div class="register-card">
        <h1>Register to NavRide</h1>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="username" id="username" required placeholder="Enter your username" />
          </div>
  
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" v-model="email" id="email" required placeholder="Enter your email" />
          </div>
  
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" id="password" required placeholder="Enter your password" />
          </div>
  
          <div class="form-group">
            <label for="confirmPassword">Confirm Password</label>
            <input type="password" v-model="confirmPassword" id="confirmPassword" required placeholder="Confirm your password" />
          </div>
  
          <div class="form-group">
            <label for="role">Role</label>
            <select v-model="role" id="role" required>
              <option value="driver">Driver</option>
              <option value="customer">Passenger</option>
            </select>
          </div>
  
          <button type="submit" :disabled="isSubmitting" class="submit-btn">Register</button>
        </form>
  
        <!-- Already have an account? -->
        <div class="redirect-link">
          <p>Already have an account? <router-link to="/login" class="link">Login here</router-link></p>
        </div>
  
        <!-- Error Message -->
        <div v-if="errorMessage" class="error-message">
          <p>{{ errorMessage }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        role: 'customer', // Default role
        errorMessage: '',
        isSubmitting: false,
      };
    },
    methods: {
      async submitForm() {
        // Check if passwords match
        if (this.password !== this.confirmPassword) {
          this.errorMessage = "Passwords don't match.";
          return;
        }
  
        this.isSubmitting = true;
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            username: this.username,
            email: this.email,
            password: this.password,
            role: this.role,
          });
  
          if (response.status === 200) {
            // Redirect to login page or dashboard
            this.$router.push('/login');
          }
        } catch (error) {
          // Display error message if registration fails
          this.errorMessage = error.response?.data?.message || 'Registration failed';
        } finally {
          this.isSubmitting = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #e0f7fa; /* Light blue background */
  }
  
  .register-card {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 400px;
    max-width: 100%;
    text-align: center;
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
    font-weight: 600;
    color: #2980b9; /* Light blue text */
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    font-weight: 500;
    display: block;
    margin-bottom: 8px;
    color: #555;
  }
  
  input,
  select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
    box-sizing: border-box;
    color: #333;
  }
  
  input:focus,
  select:focus {
    outline: none;
    border-color: #2980b9; /* Highlighted border on focus */
  }
  
  button.submit-btn {
    width: 100%;
    padding: 12px;
    background-color: #2980b9; /* Light blue button */
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button.submit-btn:disabled {
    background-color: #ddd;
    cursor: not-allowed;
  }
  
  button.submit-btn:hover {
    background-color: #e0f7fa; /* Darker blue on hover */
  }
  
  .redirect-link {
    margin-top: 15px;
  }
  
  .redirect-link p {
    font-size: 14px;
    color: #333;
  }
  
  .link {
    color: #2980b9;
    text-decoration: none;
  }
  
  .link:hover {
    text-decoration: underline;
  }
  
  .error-message {
    color: red;
    font-size: 14px;
    text-align: center;
    margin-top: 10px;
  }
  </style>
  