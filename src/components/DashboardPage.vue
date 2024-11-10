<template>
    <div class="dashboard-container p-8 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200">
      <!-- Welcome Section -->
      <div class="welcome-section mb-8">
        <h2 class="text-3xl text-blue-600 font-bold mb-4 dark:text-yellow-400">
          Welcome to NavRide, {{ username || 'Guest' }}!
        </h2>
        <p class="text-lg mb-4">
          NavRide is your go-to app for hassle-free transportation in Naval, Biliran! Whether you're heading to a meeting, running errands, or need a ride for an important event, we’ve got you covered. Our user-friendly interface ensures you can request rides and services with just a few taps.
        </p>
        <p class="text-lg mb-8">
          Our dedicated drivers are ready to provide you with a comfortable ride while ensuring your safety and convenience.
        </p>
      </div>
  
      <!-- Passenger Dashboard -->
      <div v-if="role === 'Passenger'" class="role-dashboard">
        <h3 class="text-2xl text-blue-600 font-semibold mb-4 dark:text-yellow-400">
          Your Ride Dashboard
        </h3>
        
        <!-- Upcoming Ride Section -->
        <div class="ride-info mb-6">
          <h4 class="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">
            Upcoming Ride:
          </h4>
          <p v-if="hasUpcomingRide" class="text-gray-600 dark:text-gray-300">
            Your next ride is scheduled for <strong>{{ upcomingRideDate }}</strong>. Get ready to go!
          </p>
          <p v-else class="text-gray-600 dark:text-gray-300">
            No upcoming rides. Book your next ride today!
          </p>
        </div>
  
        <!-- Favorite Drivers Section -->
        <div class="favorite-drivers mb-6">
          <h4 class="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">
            Your Favorite Drivers
          </h4>
          <p class="text-gray-600 dark:text-gray-300">
            Keep track of your favorite drivers for quicker bookings and personalized experiences.
          </p>
          <router-link to="/favorite-drivers" class="text-blue-600 hover:text-blue-700 dark:text-yellow-400 dark:hover:text-yellow-300">
            View Favorites
          </router-link>
        </div>
  
        <!-- Actions Section -->
        <div class="actions">
          <button @click="goToBookRide" class="btn-primary">
            Book a Ride
          </button>
        </div>
      </div>
  
      <!-- Rider Dashboard -->
      <div v-if="role === 'Rider'" class="role-dashboard">
        <h3 class="text-2xl text-blue-600 font-semibold mb-4 dark:text-yellow-400">
          Your Rider Dashboard
        </h3>
        
        <!-- Availability Section -->
        <div class="availability-section mb-6">
          <h4 class="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">
            Your Availability
          </h4>
          <p v-if="isAvailable" class="text-gray-600 dark:text-gray-300">
            You're available to accept rides. Your next passenger could be just a click away!
          </p>
          <p v-else class="text-gray-600 dark:text-gray-300">
            You're currently unavailable. Set yourself as available when ready.
          </p>
          <button @click="toggleAvailability" class="btn-secondary">
            {{ isAvailable ? 'Set as Unavailable' : 'Set as Available' }}
          </button>
        </div>
  
        <!-- Earnings History Section -->
        <div class="earnings-history mb-6">
          <h4 class="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">
            Your Earnings History
          </h4>
          <p class="text-gray-600 dark:text-gray-300">
            View your total earnings from completed rides, including trip details.
          </p>
          <router-link to="/earnings-history" class="text-blue-600 hover:text-blue-700 dark:text-yellow-400 dark:hover:text-yellow-300">
            View Earnings
          </router-link>
        </div>
  
        <!-- Actions Section -->
        <div class="actions">
          <button class="btn-primary">
            Accept a Ride
          </button>
        </div>
      </div>
  
      <!-- General Info Section (for both roles) -->
      <div class="general-info mt-8">
        <h4 class="text-2xl text-blue-600 font-semibold mb-4 dark:text-yellow-400">
          Features of NavRide
        </h4>
        <ul class="list-disc ml-8 text-gray-700 dark:text-gray-300">
          <li>🚗 Quick and easy ride requests for passengers.</li>
          <li>📍 Real-time tracking of rides.</li>
          <li>👍 Professional drivers who prioritize safety.</li>
          <li>💳 Simple and secure payment options.</li>
          <li>🕒 Flexible ride schedules for both passengers and riders.</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: localStorage.getItem('username') || 'Guest', // Fetch username from localStorage
        role: localStorage.getItem('role') || '',  // Fetch role from localStorage
        hasUpcomingRide: true,  // Static data for now
        upcomingRideDate: 'November 15, 2024',  // Static example
        isAvailable: true,  // Static data for availability
      };
    },
    mounted() {
      if (!this.role) {
        // If role is not found in localStorage, redirect to login
        this.$router.push('/login');
      }
    },
    methods: {
      goToBookRide() {
        this.$router.push('/book-ride');  // Redirect to ride booking page
      },
      toggleAvailability() {
        this.isAvailable = !this.isAvailable;  // Toggle availability
      },
    },
  };
  </script>
  
  <style scoped>
  .dashboard-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .role-dashboard {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
  }
  
  h3 {
    font-size: 1.8rem;
    font-weight: bold;
    color: #333;
  }
  
  h4 {
    font-size: 1.4rem;
    font-weight: semi-bold;
  }
  
  ul {
    padding-left: 20px;
  }
  
  .btn-primary {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
  }
  
  .btn-primary:hover {
    background-color: #45a049;
  }
  
  .btn-secondary {
    background-color: #007BFF;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
  }
  
  .btn-secondary:hover {
    background-color: #0056b3;
  }
  
  .general-info {
    background-color: #e7f0ff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .general-info h4 {
    color: #007bff;
  }
  </style>
  