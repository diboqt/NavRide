import { createRouter, createWebHistory } from 'vue-router';
import RegisterPage from '../components/RegisterPage.vue'; // Assuming RegisterPage.vue exists
import LoginPage from '../components/LoginPage.vue'; // Assuming LoginPage.vue exists
import DashboardPage from '../components/DashboardPage.vue'; // Redirect destination after login
import BookRide from '../components/BookaRide.vue';
import PassengerProfile from '../components/PassengerProfile.vue';
import FavoriteRiders from '../components/FavoriteRiders.vue';
import RideHistory from '../components/RideHistory.vue';
import AvailableRides from '../components/AvailableRides.vue';
import RiderHistory from '../components/RiderHistory.vue';
import EarningsHistory from '../components/EarningHistory.vue';
import DriverProfile from '../components/DriverProfile.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage
  },  {
    path: '/book-ride',
    name: 'BookRide',
    component: BookRide,
    meta: { requiresAuth: true }, // Only accessible if authenticated
  },
  {
    path: '/passenger-profile',
    name: 'PassengerProfile',
    component: PassengerProfile,
    meta: { requiresAuth: true }, // Only accessible if authenticated
  },{
    path: '/favorite-riders',
    name: 'FavoriteRiders',
    component: FavoriteRiders,
    meta: { requiresAuth: true }, // Only accessible if authenticated
  },
  {
    path: '/ride-history',
    name: 'RideHistory',
    component: RideHistory,
    meta: { requiresAuth: true }, // Only accessible if authenticated
  },
  {
    path: '/earnings-history',
    name: 'EarningsHistory',
    component: EarningsHistory,
    meta: { requiresAuth: true },
  },
  {
    path: '/driver-profile',
    name: 'DriverProfile',
    component: DriverProfile,
    meta: { requiresAuth: true },
  },{
    path: '/available-rides',
    name: 'AvailableRides',
    component: AvailableRides,
    meta: { requiresAuth: true },
  },
  {
    path: '/rider-history',
    name: 'RiderHistory',
    component: RiderHistory,
    meta: { requiresAuth: true },
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

