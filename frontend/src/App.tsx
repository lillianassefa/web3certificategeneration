// const App = () => {
//   const handleButtonClick = () => {
//     console.log('Button clicked!')
//   }
//     console.log("here");

//   return (
//     <div className="flex items-center justify-center h-screen">
//       <div className="text-center">
//         <h1 className="text-4xl font-bold mb-4">Hello Students!</h1>
//         <p className="text-lg mb-6">Press the button to get your certificate.</p>
//         <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700" onClick={handleButtonClick}>
//           Get Certificate
//         </button>
//       </div>
//     </div>
//   )
// }

// export default App
import React from 'react'
import './styles.css' // Import the generated styles from Tailwind CSS

const App: React.FC = () => {
  const handleButtonClick = () => {
    console.log('Button clicked!')
  }

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-r from-blue-400 to-indigo-500 text-white">
      <div className="text-center p-8 bg-white bg-opacity-30 rounded-md">
        <h1 className="text-4xl font-bold mb-4">Hello Students!</h1>
        <p className="text-lg mb-6">Press the button to get your certificate.</p>
        <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 focus:outline-none" onClick={handleButtonClick}>
          Get Certificate
        </button>
      </div>
    </div>
  )
}

export default App
