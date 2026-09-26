async function analyzeURL() {

    const input = document.getElementById("urlInput");

    const button = document.getElementById("analyzeButton");

    const loading = document.getElementById("loading");

    const resultCard = document.getElementById("resultCard");

    const prediction = document.getElementById("prediction");

    const probability = document.getElementById("probability");

    const progress = document.getElementById("progress");

    const message = document.getElementById("message");

    const displayURL = document.getElementById("displayURL");

    const resultIcon = document.getElementById("resultIcon");


    const url = input.value.trim();


    // Check empty input

    if (!url) {

        alert("Please enter a URL.");

        return;

    }


    // Show loading

    button.disabled = true;

    loading.classList.remove("hidden");

    resultCard.classList.add("hidden");


    try {

        const response = await fetch(
            `/predict?url=${encodeURIComponent(url)}`
        );


        if (!response.ok) {

            throw new Error(
                "Unable to analyze the URL."
            );

        }


        const data = await response.json();


        // Hide loading

        loading.classList.add("hidden");

        resultCard.classList.remove("hidden");


        // Display URL

        displayURL.textContent = data.url;


        // Display probability

        const risk = data.phishing_probability;

        probability.textContent =
            `${risk.toFixed(2)}%`;

        progress.style.width =
            `${risk}%`;


        // Display prediction

        prediction.textContent =
            data.prediction;


        // Change result message

        if (data.prediction === "PHISHING") {

            resultIcon.textContent = "🚨";

            prediction.style.color = "#ff6b6b";

            progress.style.background =
                "#ff6b6b";

            message.textContent =
                "The URL contains characteristics that resemble phishing URLs in the training data. Avoid entering sensitive information unless the website can be independently verified.";

        } else {

            resultIcon.textContent = "🛡️";

            prediction.style.color = "#4ade80";

            progress.style.background =
                "#4ade80";

            message.textContent =
                "The URL was classified as legitimate based on the characteristics analyzed by the machine learning model. This does not guarantee that the website is completely safe.";

        }


    } catch (error) {

        loading.classList.add("hidden");

        alert(
            "Something went wrong while analyzing the URL."
        );

        console.error(error);

    }


    button.disabled = false;

}