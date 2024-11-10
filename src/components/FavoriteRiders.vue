<template>
    <div class="favorite-riders-container p-8 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200">
      <h2 class="text-3xl text-blue-600 font-bold mb-6 dark:text-yellow-400">Your Favorite Riders</h2>
  
      <!-- Favorite Riders List -->
      <div class="riders-list">
        <div v-for="(rider, index) in favoriteRiders" :key="index" class="rider-card mb-6 p-6 bg-gray-50 dark:bg-gray-800 rounded-lg shadow-lg hover:shadow-xl transition-all transform hover:translate-y-2">
          <div class="rider-header flex items-center mb-4">
            <!-- Placeholder Image -->
            <img :src="rider.image" alt="Rider Image" class="w-16 h-16 rounded-full border-2 border-gray-300 mr-4">
            <div class="rider-info">
              <h3 class="text-xl text-blue-600 dark:text-yellow-400 font-semibold">{{ rider.name }}</h3>
              <p class="text-lg text-gray-700 dark:text-gray-300">Rating: {{ rider.rating }} ★</p>
            </div>
          </div>
          <div class="rider-status mb-4">
            <p v-if="rider.isAvailable" class="text-green-500 font-semibold">Currently Available</p>
            <p v-else class="text-red-500 font-semibold">Currently Unavailable</p>
          </div>
          <button class="btn-primary mt-4" @click="messageRider(rider.name)">Send Message</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        favoriteRiders: [
          {
            name: 'John Doe',
            rating: 4.8,
            image: 'https://via.placeholder.com/150', // Placeholder image
            isAvailable: true,
          },
          {
            name: 'Jane Smith',
            rating: 4.6,
            image: 'https://via.placeholder.com/150', // Placeholder image
            isAvailable: false,
          },
          {
            name: 'Robert Williams',
            rating: 5.0,
            image: 'https://via.placeholder.com/150', // Placeholder image
            isAvailable: true,
          },
        ],
      };
    },
    methods: {
      messageRider(name) {
        alert(`You can send a message to ${name}`);
        // This can later be integrated with messaging functionality
      },
    },
  };
  </script>
  
  <style scoped>
  .favorite-riders-container {
    max-width: 900px;
    margin: 0 auto;
  }
  
  .rider-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    background-color: #f9fafb; /* Light gray for better contrast */
    border-radius: 8px;
    padding: 1.5rem;
  }
  
  .rider-card:hover {
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
  
  .rider-header {
    display: flex;
    align-items: center;
  }
  
  .rider-info {
    max-width: 80%;
  }
  
  .rider-status {
    margin-top: 10px;
  }
  
  .btn-primary {
    background-color: #4caf50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .btn-primary:hover {
    background-color: #45a049;
  }
  
  img {
    object-fit: cover;
  }
  </style>
  