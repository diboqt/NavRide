<template>
    <div class="earnings-history">
      <h3 class="text-xl text-blue-600 font-semibold mb-2 dark:text-yellow-400">Earnings History</h3>
      <ul class="earnings-list">
        <li v-for="earnings in earningsHistory" :key="earnings.id" class="earnings-item mb-4 p-4 bg-white shadow-md rounded-lg">
          <p><strong>Ride:</strong> {{ earnings.ride }}</p>
          <p><strong>Date:</strong> {{ earnings.date }}</p>
          <p><strong>Amount:</strong> ${{ earnings.amount.toFixed(2) }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        earningsHistory: [
          { id: 1, ride: "Downtown to Airport", date: "2024-10-30", amount: 50 },
          { id: 2, ride: "Uptown to Mall", date: "2024-10-25", amount: 20 },
          { id: 3, ride: "Central Park to Museum", date: "2024-10-20", amount: 15 },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .earnings-item {
    background-color: #fff;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .earnings-list {
    list-style-type: none;
    padding-left: 0;
  }
  
  .earnings-list li {
    margin-bottom: 15px;
  }
  
  .earnings-item p {
    margin-bottom: 5px;
  }
  
  .earnings-item p strong {
    font-weight: 600;
  }
  </style>
  