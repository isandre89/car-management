const updateTotal = () => {
  const rows = document.querySelectorAll("tbody tr");
  rows.forEach((row) => {
    const productionCosts = parseFloat(
      row.querySelector('.cell input[name$="production_costs"]').value || 0
    );
    const transportationCosts = parseFloat(
      row.querySelector('.cell input[name$="transportation_costs"]').value || 0
    );

    const totalInput = row.querySelector(".total-input");
    const total = productionCosts + transportationCosts;

    totalInput.value = total.toFixed(2);
  });
};

const costInputs = document.querySelectorAll(
  '.cell input[name$="production_costs"], .cell input[name$="transportation_costs"]'
);

costInputs.forEach((input) => {
  input.addEventListener("input", updateTotal);
});

updateTotal();
