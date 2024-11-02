/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      dark: {
        100: '#000000',
      },
      white: {
        100: '#FFFFFF',
      },
      brown: {
        100: '#5A322A',
        200: '#1F1312',
        300: '#190F0E',
      },
      yellow: {
        100: '#E6A313',
      },
      orange: {
        100: '#DB500F',
      },
      red: {
        100: '#D3180D',
      },
      gray: {
        100: '#9BA5A3',
      },
      pink: {
        100: '#CAA99D',
      },
    },
    fontFamily: {
      montserrat: ['Montserrat'],
    },
  },
  plugins: [],
}
