<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <h2>NavRide</h2>
      <p>Welcome, {{ username || capitalizeRole(role) || 'Guest' }}!</p>
    </div>

    <div class="sidebar-menu">
      <ul>
        <li v-if="role === 'passenger'">
          <router-link to="/passenger-profile">Profile</router-link>
        </li>
        <li v-if="role === 'passenger'">
          <router-link to="/book-ride">Book a Ride</router-link>
        </li>
        <li v-if="role === 'passenger'">
          <router-link to="/ride-history">Ride History</router-link>
        </li>
        <li v-if="role === 'passenger'">
          <router-link to="/favorite-riders">Favorite Drivers</router-link>
        </li>
        <li v-if="role === 'rider'">
          <router-link to="/driver-profile">Profile</router-link>
        </li>
        <li v-if="role === 'rider'">
          <router-link to="/available-rides">Available Rides</router-link>
        </li>
        <li v-if="role === 'rider'">
          <router-link to="/rider-history">Rider History</router-link>
        </li>
        <li v-if="role === 'rider'">
          <router-link to="/earnings-history">Earnings History</router-link>
        </li>
      </ul>
    </div>

    <div class="sidebar-footer">
      <button v-if="username" @click="logout" class="logout-btn">Logout</button>
      <router-link v-else to="/login" class="logout-btn">Login</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || '',
      role: localStorage.getItem('role') || '',
    };
  },
  methods: {
    capitalizeRole(role) {
      if (!role) return '';
      return role.charAt(0).toUpperCase() + role.slice(1).toLowerCase();
    },
    logout() {
      localStorage.removeItem('auth_token');
      localStorage.removeItem('username');
      localStorage.removeItem('role');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.sidebar {
  width: 260px;
  height: 100vh;
  background-color: #87ceeb; /* Sky blue background for sidebar */
  color: #1976d2; /* Slightly darker blue text for contrast */
  padding: 2rem 1.5rem;
  position: fixed;
  left: 0;
  top: 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 1000;
}

.sidebar-header {
  margin-bottom: 2rem;
  text-align: center;
}

.sidebar-header h2 {
  font-size: 2.2rem;
  font-weight: 700;
  color: #1976d2;
  margin-bottom: 0.5rem;
}

.sidebar-header p {
  font-size: 1.2rem;
  font-weight: 500;
  color: #2196f3;
}

.sidebar-menu ul {
  list-style-type: none;
  padding: 0;
}

.sidebar-menu li {
  margin: 1.2rem 0;
}

.sidebar-menu a {
  color: #1976d2;
  text-decoration: none;
  font-size: 1.3rem;
  display: block;
  padding: 0.6rem;
  border-radius: 5px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.sidebar-menu a:hover {
  background-color: #b3e0ff; /* Light hover effect for sky blue */
  color: #0d47a1; /* Darker blue on hover */
}

.sidebar-footer {
  margin-top: auto;
  text-align: center;
}

.logout-btn {
  padding: 0.9rem 2.5rem;
  margin-top: 2rem;
  font-size: 1.2rem;
  color: white;
  background-color: #e57373;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-btn:hover {
  background-color: #c62828; /* Darker red on hover */
}
</style>
