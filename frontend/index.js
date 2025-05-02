// Fetch and render COVID cases line chart
axios.get("http://127.0.0.1:8000/cases")
    .then(res => {
        const data = res.data;
        const countries = data.map(row => row.country);
        const cases = data.map(row => row.total_infected);
        const trace = {
            x: countries,
            y: cases,
            type: 'bar',
            marker: {
                color: 'red'
            },
            width: 0.8
        };
        Plotly.newPlot("cases-chart", [trace], {
            title: "COVID Cases by Country (Jan 2020 - Sep 2023)",
            xaxis: {
                title: "Country",
                tickangle: -45,
                tickfont: {
                    size: 9
                },
                automargin: true
            },
            yaxis: {
                title: "Total Cases"
            },
            margin: {
                b: 100 // extra bottom space for labels
            }
        });
    })
    .catch(err => console.error("Error fetching /cases:", err));

// Fetch and render geo-map chart
axios.get("http://127.0.0.1:8000/cases")
    .then(res => {
        const data = res.data;

        const trace = {
            type: "choropleth",
            locationmode: "country names",
            locations: data.map(r => r.country),
            z: data.map(r => r.total_infected),
            text: data.map(r => `${r.country}: ${r.total_infected}`),
            colorscale: [
                [0, "rgba(255, 0, 0, 0.1)"],
                [1, "rgb(86, 97, 199)"]
            ],
            colorbar: {
                title: "Total Cases",
                tickprefix: "",
                thickness: 15
            },
            marker: {
                line: {
                    color: "rgb(255,255,255)",
                    width: 0.5
                }
            }
        };

        Plotly.newPlot("map-chart", [trace], {
            title: "COVID Case Density by Country",
            geo: {
                scope: "world",
                projection: { type: "natural earth" },
                showland: true,
                landcolor: "rgb(217, 217, 217)"
            }
        });
    })
    .catch(err => console.error("Error fetching /cases:", err));