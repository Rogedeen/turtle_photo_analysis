/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        turtle: {
          50: '#f2fbf5',
          100: '#e1f6e8',
          200: '#c3ecd4',
          300: '#95dbb4',
          400: '#5fc28e',
          500: '#3ba473',
          600: '#2c835b',
          700: '#25694a',
          800: '#20533c',
          900: '#1b4433',
          950: '#0e261d',
        }
      }
    },
  },
  plugins: [],
}
