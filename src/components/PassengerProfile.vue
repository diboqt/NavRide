<template>
  <div class="profile-container p-8 bg-lightblue text-darkblue dark:bg-gray-900 dark:text-gray-200">
    <div class="profile-header mb-8">
      <h2 class="text-3xl font-bold mb-4 dark:text-yellow-400">Your Profile</h2>
      <p class="text-lg mb-4">Manage your personal information, view your ride history, and more!</p>
    </div>

    <!-- Profile Information Section -->
    <div class="profile-info mb-8">
      <h3 class="text-2xl font-semibold mb-4 dark:text-yellow-400">Personal Information</h3>

      <div class="profile-details p-6 rounded-lg shadow-lg bg-white dark:bg-gray-800">
        <div class="profile-field mb-4">
          <label for="username" class="text-sm font-medium text-gray-600 dark:text-gray-300">Username</label>
          <p id="username" class="text-lg">{{ username }}</p>
        </div>

        <div class="profile-field mb-4">
          <label for="email" class="text-sm font-medium text-gray-600 dark:text-gray-300">Email</label>
          <p id="email" class="text-lg">{{ email }}</p>
        </div>

        <div class="profile-field mb-4">
          <label for="phone" class="text-sm font-medium text-gray-600 dark:text-gray-300">Phone Number</label>
          <p id="phone" class="text-lg">{{ phoneNumber }}</p>
        </div>

        <button @click="editProfile" class="btn-primary">
          Edit Profile
        </button>
      </div>
    </div>

    <!-- Ride History Section -->
    <div class="ride-history mb-8">
      <h3 class="text-2xl font-semibold mb-4 dark:text-yellow-400">Your Ride History</h3>
      <div v-if="rideHistory.length === 0" class="text-gray-600 dark:text-gray-300">
        You have no ride history yet. Book your first ride today!
      </div>
      <div v-else class="ride-history-list">
        <ul class="list-disc pl-5 text-darkblue dark:text-gray-200">
          <li v-for="ride in rideHistory" :key="ride.id" class="mb-2">
            <strong>{{ ride.date }}</strong> - Ride from <em>{{ ride.from }}</em> to <em>{{ ride.to }}</em>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || 'Guest', 
      email: 'passenger@example.com',
      phoneNumber: '+1234567890',
      rideHistory: [
        { id: 1, date: 'November 10, 2024', from: 'Naval, Biliran', to: 'Cabanatuan, Leyte' },
        { id: 2, date: 'November 12, 2024', from: 'Biliran, Naval', to: 'Tacloban City' },
        { id: 3, date: 'November 14, 2024', from: 'Naval, Biliran', to: 'Ormoc City' }
      ],
    };
  },
  methods: {
    editProfile() {
      this.$router.push('/edit-profile');
    },
  },
};
</script>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: 0 auto;
  background-color: #e3f2fd; /* Light blue */
  color: #1976d2; /* Dark blue */
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-header {
  text-align: center;
}

.profile-info {
  background-color: #ffffff; /* White background for light mode */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-details {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.profile-field {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2980b9;
}

.text-lg {
  font-size: 1.125rem;
}

.btn-primary {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%;
  margin-top: 20px;
}

.btn-primary:hover {
  background-color: #45a049;
}

.ride-history-list {
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 8px;
}
</style>
