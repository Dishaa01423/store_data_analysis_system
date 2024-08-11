document.addEventListener('DOMContentLoaded', function() {
    fetchData('/api/monthly_revenue', 'monthly-revenue-chart', 'line');
    fetchData('/api/product_revenue', 'product-revenue-chart', 'bar');
    fetchData('/api/customer_revenue', 'customer-revenue-chart', 'bar');
    fetchTopCustomers();
});

function fetchData(url, elementId, chartType) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            createChart(elementId, data, chartType);
        })
        .catch(error => console.error('Error:', error));
}

function createChart(elementId, data, chartType) {
    const ctx = document.getElementById(elementId).getContext('2d');
    new Chart(ctx, {
        type: chartType,
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Revenue',
                data: Object.values(data),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function fetchTopCustomers() {
    fetch('/api/top_customers')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('top-customers-list');
            Object.entries(data).forEach(([customer, revenue]) => {
                const listItem = document.createElement('p');
                listItem.textContent = `${customer}: $${revenue.toFixed(2)}`;
                list.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error:', error));
}
