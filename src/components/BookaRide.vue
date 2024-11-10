<template>
    <div class="book-ride-container p-8 bg-lightblue text-darkblue dark:bg-gray-900 dark:text-gray-200">
      <h2 class="text-3xl text-blue-600 font-bold mb-6 dark:text-yellow-400">Book a Ride</h2>
    
      <!-- Current Location and Selected Destination -->
      <div class="location-section flex mb-8">
        <div class="current-location flex-1 mr-6">
          <h3 class="text-xl text-blue-600 font-semibold mb-2 dark:text-yellow-400">Your Current Location</h3>
          <p v-if="currentLocation" class="text-lg">{{ currentLocation.latitude }}, {{ currentLocation.longitude }}</p>
          <button @click="getLocation" class="btn-primary">Get Current Location</button>
        </div>
    
        <div class="selected-destination flex-1">
          <h3 class="text-xl text-blue-600 font-semibold mb-2 dark:text-yellow-400">Selected Destination</h3>
          <p v-if="selectedDestination" class="text-lg">{{ selectedDestination.lat }}, {{ selectedDestination.lng }}</p>
        </div>
      </div>
    
      <div id="map" class="map-container mb-6"></div>
    
      <button v-if="selectedDestination" @click="bookRide" class="btn-primary">
        Book Ride
      </button>
    </div>
  </template>
  
  <script>
  import L from "leaflet";
  import "leaflet/dist/leaflet.css";
  
  export default {
    data() {
      return {
        currentLocation: null,
        selectedDestination: null,
        map: null,
      };
    },
    mounted() {
      this.initMap();
    },
    methods: {
      getLocation() {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.currentLocation = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude,
            };
            this.centerMapOnLocation(this.currentLocation.latitude, this.currentLocation.longitude);
          },
          (error) => alert("Error getting location: " + error.message)
        );
      },
      initMap() {
        this.map = L.map("map", { scrollWheelZoom: false }).setView([0, 0], 2);
  
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution: '© OpenStreetMap contributors',
        }).addTo(this.map);
  
        this.map.once("click", (e) => {
          this.selectedDestination = { lat: e.latlng.lat, lng: e.latlng.lng };
          L.marker([e.latlng.lat, e.latlng.lng]).addTo(this.map).bindPopup("Destination").openPopup();
        });
      },
      centerMapOnLocation(lat, lng) {
        if (this.map) {
          this.map.setView([lat, lng], 13);
          L.marker([lat, lng]).addTo(this.map).bindPopup("You are here").openPopup();
        }
      },
      bookRide() {
        alert(`Booking ride to ${this.selectedDestination.lat}, ${this.selectedDestination.lng}`);
      },
    },
    beforeUnmount() {
      if (this.map) this.map.remove();
    },
  };
  </script>
  
  <style scoped>
  .book-ride-container {
    max-width: 900px;
    margin: 0 auto;
    background-color: #e3f2fd; /* Light blue */
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .location-section {
    display: flex;
    gap: 2rem;
    justify-content: space-between;
  }
  
  .current-location, .selected-destination {
    flex: 1;
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  h3 {
    font-size: 1.25rem;
    color: #2980b9;
  }
  
  .btn-primary {
    background-color: #4caf50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    margin-top: 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 100%;
  }
  
  .btn-primary:hover {
    background-color: #45a049;
  }
  
  .map-container {
    width: 100%;
    height: 400px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  </style>
  