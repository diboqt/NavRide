<template>
    <div class="available-rides">
      <h3 class="available-rides-title">Available Rides</h3>
      <ul class="ride-list">
        <li v-for="ride in availableRides" :key="ride.id" class="ride-item">
          <div class="ride-info">
            <p><strong>From:</strong> {{ ride.from }}</p>
            <p><strong>To:</strong> {{ ride.to }}</p>
            <p><strong>Distance:</strong> {{ ride.distance }} km</p>
          </div>
          <button @click="acceptRide(ride)" class="btn-accept">Accept Ride</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        availableRides: [
  { id: 1, from: "Naval", to: "Caibiran", distance: 16 },
  { id: 2, from: "Naval", to: "Biliran", distance: 10 },
  { id: 3, from: "Caibiran", to: "Almeria", distance: 8 },
  { id: 4, from: "Naval", to: "Kawayan", distance: 12 },
  { id: 5, from: "Biliran", to: "Naval", distance: 10 },
  { id: 6, from: "Biliran", to: "Dagohoy Falls", distance: 7 },
]

      };
    },
    methods: {
      acceptRide(ride) {
        alert(`You have accepted the ride from ${ride.from} to ${ride.to}`);
        // Add actual functionality for accepting a ride here
      },
    },
  };
  </script>
  
  <style scoped>
  .available-rides {
    padding: 20px;
    background-color: #e6f7ff; /* Light blue background */
    border-radius: 8px;
  }
  
  .available-rides-title {
    font-size: 24px;
    color: #2980b9; /* Blue color for title */
    font-weight: 600;
    margin-bottom: 20px;
  }
  
  .ride-list {
    list-style-type: none;
    padding-left: 0;
  }
  
  .ride-item {
    background-color: #fff;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .ride-info p {
    margin-bottom: 8px;
    font-size: 16px;
    color: #333;
  }
  
  .ride-info strong {
    color: #2980b9;
  }
  
  .btn-accept {
    padding: 12px 20px;
    background-color: #007bff; /* Primary blue color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    margin-top: 15px;
    width: 150px;
    text-align: center;
    transition: background-color 0.3s ease;
  }
  
  .btn-accept:hover {
    background-color: #0056b3;
  }
  
  .btn-accept:disabled {
    background-color: #d6d6d6;
    cursor: not-allowed;
  }
  </style>
  