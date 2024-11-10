<template>
  <div id="app">
    <!-- Sidebar only visible on non-register and non-login pages -->
    <div v-if="!isRegisterOrLoginPage">
      <Sidebar />
    </div>
    
    <!-- Main Content Area -->
    <div class="content-container">
      <router-view />
    </div>
  </div>
</template>

<script>
import Sidebar from './components/SideBar.vue'; // Import your Sidebar component

export default {
  components: {
    Sidebar,
  },
  computed: {
    // Check if current route is register or login page
    isRegisterOrLoginPage() {
      return this.$route.name === 'Register' || this.$route.name === 'Login';
    }
  }
};
</script>

<style scoped>
/* App container */
#app {
  display: flex;
  min-height: 100vh;
  margin: 0;
  padding: 0;
  background-color: #e0f7fa; /* Light blue background for the app */
}

/* Sidebar style */
.sidebar {
  width: 250px;
  padding: 20px;
  box-sizing: border-box;
  position: fixed;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 10;
  background-color: #ffffff; /* White sidebar for contrast */
  color: #00796b; /* Slightly darker teal for text */
}

/* Content area style */
.content-container {
  margin-left: 250px; /* Space for the sidebar */
  padding: 20px;
  width: calc(100% - 250px);
  height: 100vh;
  overflow-y: auto;
  box-sizing: border-box;
  color: #00796b; /* Text color for readability */
  background-color: #e0f7fa; /* Match app background */
}

/* Styling Links */
.sidebar a {
  color: #00796b; /* Matches the darker teal text */
  text-decoration: none;
}

.sidebar a:hover {
  color: #004d40; /* Slightly darker shade for hover effect */
}

/* Button Styling */
.logout-btn {
  background-color: #00796b;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.logout-btn:hover {
  background-color: #004d40;
}
</style>
