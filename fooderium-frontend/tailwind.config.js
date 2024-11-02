/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
    colors: {
      'main-brown': '#1F1312',
      'accent-yellow': '#E6A313',
      'accent-orange': '#DB500F',
      'accent-red': '#D3180D',
      'bgbd-gray': '#9BA5A3',
      'main-brown-footer': '#5A322A',
      'main-brown-darker': '#190F0E',
      'bd-pink': 'CAA99D',
    },
    fontFamily: {
      sans: ['Montserrat', 'sans-serif'],
    },
  },
  plugins: [],
}
