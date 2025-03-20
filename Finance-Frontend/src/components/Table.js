export function Table({ data }) {
  // Check if data is non-empty, otherwise return empty table or a message
  if (data.length === 0) {
    return <div>No data available</div>;
  }

  // Get the column names (keys of the first object in the data array)
  const columns = Object.keys(data[0]);

  return (
    <table style={{ borderCollapse: "collapse", width: "100%" }}>
      <thead>
        <tr>
          {columns.map((column) => (
            <th
              key={column}
              style={{
                border: "1px solid #ddd",
                padding: "8px",
                textAlign: "left",
              }}
            >
              {column.charAt(0).toUpperCase() + column.slice(1)}{" "}
              {/* Capitalize first letter */}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            {columns.map((column) => (
              <td
                key={column}
                style={{
                  border: "1px solid #ddd",
                  padding: "8px",
                  textAlign: "left",
                }}
              >
                {row[column]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
