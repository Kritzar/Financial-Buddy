import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Tooltip,
  Legend,
  Filler,
} from "chart.js";
import annotationPlugin from "chartjs-plugin-annotation";

ChartJS.register(
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Title,
  Tooltip,
  Legend,
  Filler,
  annotationPlugin
);

const LineChart = ({ dataInput, deviationThreshold }) => {
  // Extract labels (dates) and data (amounts) from the input array
  const labels = dataInput.map((item) => item.date); // Extract dates
  const dataPoints = dataInput.map((item) => +item.amount); // Extract amounts as numbers

  // Calculate the average value
  const averageTemp =
    dataPoints.reduce((sum, temp) => sum + temp, 0) /
    (dataPoints.length ? dataPoints.length : 1);

  // Find min and max for Y axis
  const minY = Math.min(...dataPoints) - 2;
  const maxY = Math.max(...dataPoints) + 2;

  // Identify points that deviate significantly from the average
  const pointStyles = dataPoints.map((temp) =>
    Math.abs(temp - averageTemp) > deviationThreshold
      ? "red"
      : "rgba(75, 192, 192, 1)"
  );

  // Prepare the chart data object
  const data = {
    labels, // Dates
    datasets: [
      {
        label: "Amount",
        data: dataPoints,
        fill: true,
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 2,
        tension: 0.4,
        pointBackgroundColor: pointStyles, // Conditional point styles
        pointBorderColor: pointStyles,
        pointRadius: pointStyles.map((color) => (color === "red" ? 5 : 0)), // Larger points for deviations
      },
    ],
  };

  // Define chart options
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top",
      },
      annotation: {
        annotations: {
          averageLine: {
            type: "line",
            yMin: averageTemp,
            yMax: averageTemp,
            borderColor: "orange",
            borderWidth: 2,
            label: {
              content: `Average: ${averageTemp.toFixed(2)}°`,
              enabled: true,
              position: "end",
            },
          },
        },
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        min: minY,
        max: maxY,
      },
      x: {
        type: "category", // Use category scale for date labels
        title: {
          display: true,
          text: "Date",
        },
        ticks: {
          autoSkip: true, // Automatically skip labels if there are too many
          maxRotation: 45, // Rotate the labels if needed for readability
          minRotation: 30, // Prevent the labels from being too horizontal
        },
      },
    },
  };

  return <Line data={data} options={options} />;
};

export default LineChart;
