<template>
    <div class="ride-history-container p-8 bg-lightblue dark:bg-gray-900 text-darkblue dark:text-gray-200">
      <h2 class="text-3xl text-blue-600 font-bold mb-8 dark:text-yellow-400">Your Ride History</h2>
  
      <!-- Ride History List -->
      <div class="ride-list">
        <div v-for="(ride, index) in rideHistory" :key="index" class="ride-card mb-6 p-6 bg-gray-50 dark:bg-gray-800 rounded-lg shadow-lg hover:shadow-xl transition-all transform hover:translate-y-2">
          <div class="ride-header flex justify-between items-center mb-4">
            <div class="ride-details">
              <h3 class="text-xl text-blue-600 dark:text-yellow-400 font-semibold">{{ ride.date }}</h3>
              <p class="text-lg text-gray-700 dark:text-gray-300">{{ ride.pickupLocation }} → {{ ride.destination }}</p>
            </div>
            <div class="ride-status">
              <span :class="ride.statusClass" class="status-label">{{ ride.status }}</span>
            </div>
          </div>
          <p class="text-gray-700 dark:text-gray-300">{{ ride.additionalInfo }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        rideHistory: [
          {
            date: 'November 1, 2024',
            pickupLocation: 'Naval City Hall',
            destination: 'Biliran Provincial Hospital',
            status: 'Completed',
            statusClass: 'bg-green-500',
            additionalInfo: 'Your ride was completed successfully.',
          },
          {
            date: 'October 20, 2024',
            pickupLocation: 'Biliran Airport',
            destination: 'Naval Port',
            status: 'Cancelled',
            statusClass: 'bg-red-500',
            additionalInfo: 'The ride was cancelled by the driver.',
          },
          {
            date: 'October 15, 2024',
            pickupLocation: 'Biliran Market',
            destination: 'Naval City Hall',
            status: 'In Progress',
            statusClass: 'bg-yellow-500',
            additionalInfo: 'Your ride is currently in progress.',
          },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .ride-history-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #e3f2fd; /* Light blue */
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .ride-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    background-color: #f9fafb; /* Light gray for better contrast */
    border-radius: 8px;
    padding: 1.5rem;
  }
  
  .ride-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  
  .status-label {
    padding: 6px 12px;
    border-radius: 5px;
    color: white;
    font-weight: 600;
    text-transform: capitalize;
  }
  
  .bg-green-500 {
    background-color: #28a745;
  }
  
  .bg-red-500 {
    background-color: #dc3545;
  }
  
  .bg-yellow-500 {
    background-color: #ffc107;
  }
  
  .ride-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .ride-details {
    max-width: 70%;
  }
  
  .ride-status {
    text-align: right;
  }
  
  h3 {
    font-size: 1.25rem;
  }
  
  p {
    font-size: 1rem;
    color: #6c757d;
  }
  
  .text-lg {
    font-size: 1.125rem;
  }
  
  .text-xl {
    font-size: 1.375rem;
  }
  </style>
  