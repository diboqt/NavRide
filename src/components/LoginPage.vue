<template>
    <div class="login-container">
      <div class="welcome-text">
        <h1>Welcome to Navride</h1>
        <p class="subheading">Please log in to continue</p>
      </div>
  
      <form @submit.prevent="submitForm" class="login-form">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="email" id="email" required placeholder="Enter your email" />
        </div>
  
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" v-model="password" id="password" required placeholder="Enter your password" />
        </div>
  
        <button type="submit" :disabled="isSubmitting" class="submit-button">Login</button>
      </form>
  
      <div class="redirect-link">
        <p>Don't have an account? <router-link to="/register" class="link">Register here</router-link></p>
      </div>
  
      <!-- Error Message -->
      <div v-if="errorMessage" class="error-message">
        <p>{{ errorMessage }}</p>
      </div>
  
      <!-- Temporary Bypass Login Buttons -->
      <div class="role-buttons">
        <button @click="loginAsPassenger" class="role-button">Login as Passenger</button>
        <button @click="loginAsRider" class="role-button">Login as Rider</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        errorMessage: '',
        isSubmitting: false,
      };
    },
    methods: {
      async submitForm() {
        this.isSubmitting = true;
        this.errorMessage = ''; // Reset error message on each submission attempt
  
        try {
          // Get CSRF token if it's needed
          const csrfToken = this.getCookie('csrftoken');
  
          // Make the login request
          const response = await axios.post('http://127.0.0.1:8000/api/login/', {
            email: this.email,
            password: this.password,
          }, {
            headers: {
              'X-CSRFToken': csrfToken,  // Include CSRF token
            },
          });
  
          // Check if login is successful and store user info if needed
          if (response.status === 200) {
            // Redirect to dashboard
            this.$router.push('/dashboard');
          }
        } catch (error) {
          // Display error message if login fails
          this.errorMessage = error.response?.data?.message || 'Login failed';
        } finally {
          this.isSubmitting = false;
        }
      },
  
      loginAsPassenger() {
        // Simulate login as Passenger by saving role to localStorage
        localStorage.setItem('role', 'passenger');  // Save role as 'passenger'
        localStorage.setItem('email', 'passenger@navride.com');  // Temp email for Passenger
  
        // Redirect to the dashboard (or another route you want)
        this.$router.push('/dashboard');
      },
  
      loginAsRider() {
        // Simulate login as Rider by saving role to localStorage
        localStorage.setItem('role', 'rider');  // Save role as 'rider'
        localStorage.setItem('email', 'rider@navride.com');  // Temp email for Rider
  
        // Redirect to the dashboard (or another route you want)
        this.$router.push('/dashboard');
      },
  
      // Function to get the CSRF token from cookies
      getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
      },
    },
  };
  </script>
  
  <style scoped>
  .login-container {
    width: 100%;
    max-width: 420px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .welcome-text {
    text-align: center;
    margin-bottom: 1.5rem;
  }
  
  .welcome-text h1 {
    font-size: 2.2rem;
    color: #2980b9;
    font-weight: 600;
  }
  
  .welcome-text .subheading {
    font-size: 1.1rem;
    color: #555;
    margin-top: 0.5rem;
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 1.2rem;
  }
  
  label {
    display: block;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  input[type='email'],
  input[type='password'] {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    color: #333;
  }
  
  button.submit-button {
    width: 100%;
    padding: 1rem;
    background-color: #2980b9;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    margin-top: 1rem;
  }
  
  button.submit-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .redirect-link {
    margin-top: 1.5rem;
    text-align: center;
  }
  
  .redirect-link p {
    font-size: 0.9rem;
    color: #555;
  }
  
  .link {
    color: #2980b9;
    text-decoration: none;
    font-weight: 500;
  }
  
  .link:hover {
    text-decoration: underline;
  }
  
  .error-message {
    margin-top: 1.5rem;
    padding: 1rem;
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    border-radius: 5px;
    text-align: center;
  }
  
  /* New style for temporary role login buttons */
  .role-buttons {
    margin-top: 1.5rem;
    display: flex;
    justify-content: space-between;
  }
  
  .role-button {
    padding: 1rem;
    background-color: #27ae60;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    flex: 1;
    margin-right: 10px;
  }
  
  .role-button:last-child {
    margin-right: 0;
  }
  
  .role-button:hover {
    background-color: #2ecc71;
  }
  </style>
  