<template>
    <div class="profile-container">
      <h3 class="profile-title">Your Profile</h3>
      <div class="profile-card">
        <div class="profile-details">
          <p><strong>Name:</strong> {{ userProfile.name }}</p>
          <p><strong>Email:</strong> {{ userProfile.email }}</p>
          <p><strong>Phone:</strong> {{ userProfile.phone }}</p>
          <p v-if="userProfile.role === 'driver'"><strong>License Plate:</strong> {{ userProfile.vehiclePlate }}</p>
          <p><strong>Rating:</strong> {{ userProfile.rating }} ⭐</p>
  
          <!-- Active/Inactive Button -->
          <button 
            :class="['status-button', { 'inactive': !isActive, 'active': isActive }]" 
            @click="toggleActiveStatus">
            {{ isActive ? 'Active' : 'Inactive' }}
          </button>
  
          <button @click="editProfile" class="edit-button">Edit Profile</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userProfile: {
          name: "John Doe",
          email: "johndoe@example.com",
          phone: "+1234567890",
          role: "driver", // Or "customer"
          vehiclePlate: "ABC 1234", // Only for drivers
          rating: 4.8,
        },
        isActive: true, // Initial status is active
      };
    },
    methods: {
      toggleActiveStatus() {
        // Toggle the driver's active status
        this.isActive = !this.isActive;
      },
      editProfile() {
        // Redirect to edit profile page or open modal
        this.$router.push('/edit-profile');
      }
    }
  };
  </script>
  
  <style scoped>
  .profile-container {
    padding: 20px;
    background-color: #e6f7ff; /* Light blue background */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .profile-title {
    font-size: 24px;
    color: #2980b9;
    font-weight: 600;
    margin-bottom: 20px;
  }
  
  .profile-card {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .profile-details p {
    margin-bottom: 10px;
    font-size: 16px;
    color: #333;
  }
  
  .profile-details strong {
    color: #2980b9;
  }
  
  .status-button {
    padding: 12px 20px;
    border: 2px solid transparent;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    text-transform: uppercase;
    margin-top: 15px;
    width: 150px;
    display: inline-block;
  }
  
  .status-button.active {
    background-color: #27ae60; /* Green when active */
    color: white;
    border-color: #27ae60;
  }
  
  .status-button.inactive {
    background-color: #e74c3c; /* Red when inactive */
    color: white;
    border-color: #e74c3c;
  }
  
  .status-button:hover {
    opacity: 0.9;
  }
  
  .edit-button {
    margin-top: 20px;
    padding: 10px 15px;
    background-color: #2980b9;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .edit-button:hover {
    background-color: #3498db;
  }
  </style>
  