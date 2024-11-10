<template>
  <div class="dashboard-container">
    <div class="welcome-section">
      <h1>Welcome, {{ username || 'Guest' }}!</h1>
      <p class="role-text">You're currently logged in as a <strong>{{ role }}</strong>.</p>
    </div>

    <div class="availability-section">
      <h2>Your Availability</h2>
      <p v-if="isAvailable">You are currently available for rides. Ready to accept new trips!</p>
      <p v-else>You are not available right now. Change your status to available when you're ready.</p>
    </div>

    <div class="rides-section">
      <h2>Available Rides</h2>
      <p>View the list of available rides that you can accept.</p>
      <router-link to="/available-rides">See Available Rides</router-link>
    </div>

    <div class="earnings-history">
      <h2>Your Earnings History</h2>
      <p>Keep track of your earnings from completed rides.</p>
      <router-link to="/earnings-history">View Earnings</router-link>
    </div>

    <div class="actions">
      <button class="change-availability-button" @click="toggleAvailability">{{ isAvailable ? 'Set as Unavailable' : 'Set as Available' }}</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || 'Guest',
      role: localStorage.getItem('role') || 'Rider',  // Get the role from localStorage
      isAvailable: true,  // Static data for availability
    };
  },
  methods: {
    toggleAvailability() {
      this.isAvailable = !this.isAvailable;  // Toggle availability status
    },
  },
};
</script>

<style scoped>
.dashboard-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.welcome-section {
  text-align: center;
  margin-bottom: 2rem;
}

.welcome-section h1 {
  font-size: 2rem;
  color: #2980b9;
}

.role-text {
  font-size: 1.1rem;
  color: #555;
}

.availability-section, .rides-section, .earnings-history {
  margin-bottom: 2rem;
}

h2 {
  font-size: 1.5rem;
  color: #2980b9;
}

p {
  font-size: 1.1rem;
  color: #555;
}

.router-link {
  color: #2980b9;
  font-weight: 500;
  text-decoration: none;
}

.router-link:hover {
  text-decoration: underline;
}

.change-availability-button {
  width: 100%;
  padding: 1rem;
  background-color: #2980b9;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  cursor: pointer;
}
</style>
