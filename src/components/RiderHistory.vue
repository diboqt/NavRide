<template>
    <div class="rider-history">
      <h3 class="text-xl text-blue-600 font-semibold mb-2 dark:text-yellow-400">Rider History</h3>
      <ul class="history-list">
        <li v-for="history in riderHistory" :key="history.id" class="history-item mb-4 p-4 bg-white shadow-md rounded-lg">
          <p><strong>Ride:</strong> {{ history.ride }}</p>
          <p><strong>Date:</strong> {{ history.date }}</p>
          <p><strong>Status:</strong> 
            <span :class="{'text-green-500': history.status === 'Completed', 'text-red-500': history.status === 'Cancelled'}">
              {{ history.status }}
            </span>
          </p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        riderHistory: [
          { id: 1, ride: "Downtown to Airport", date: "2024-10-30", status: "Completed" },
          { id: 2, ride: "Uptown to Mall", date: "2024-10-25", status: "Completed" },
          { id: 3, ride: "Central Park to Museum", date: "2024-10-20", status: "Cancelled" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .history-item {
    background-color: #fff;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .history-list {
    list-style-type: none;
    padding-left: 0;
  }
  
  .history-list li {
    margin-bottom: 15px;
  }
  
  .history-item p {
    margin-bottom: 5px;
  }
  
  .history-item p strong {
    font-weight: 600;
  }
  
  .text-green-500 {
    color: #38a169; /* Green for Completed */
  }
  
  .text-red-500 {
    color: #e53e3e; /* Red for Cancelled */
  }
  </style>
  