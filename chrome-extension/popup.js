document.addEventListener("DOMContentLoaded", () => {
    const apiTypeElement = document.getElementById("api-type");
    const inputTextElement = document.getElementById("input-text");
    const languageInputElement = document.getElementById("language-input");
    const submitButton = document.getElementById("submit-btn");
    const resultContainer = document.getElementById("result-text");
  
    // Dynamically show/hide language input based on API type
    apiTypeElement.addEventListener("change", () => {
      const selectedApi = apiTypeElement.value;
      if (selectedApi === "translate") {
        languageInputElement.style.display = "block";
      } else {
        languageInputElement.style.display = "none";
      }
    });
  
    // Submit button handler
    submitButton.addEventListener("click", async () => {
      const apiType = apiTypeElement.value;
      const inputText = inputTextElement.value.trim();
      const targetLanguage = document.getElementById("language").value.trim();
  
      if (!inputText) {
        alert("Input text cannot be empty!");
        return;
      }
  
      let endpoint = "";
      let requestBody = {};
  
      // Define the endpoint and request payload based on the selected API type
      switch (apiType) {
        case "fact-check":
          endpoint = "/api/v1/tools/fact-check";
          requestBody = { text: inputText };
          break;
        case "simplify":
          endpoint = "/api/v1/tools/simplify";
          requestBody = { text: inputText };
          break;
        case "translate":
          if (!targetLanguage) {
            alert("Please provide a target language for translation!");
            return;
          }
          endpoint = "/api/v1/translation/translate";
          requestBody = { text: inputText, target_language: targetLanguage };
          break;
        case "market-analysis":
          endpoint = "/api/v1/market/market-analysis";
          requestBody = { idea: inputText };
          break;
        default:
          alert("Invalid API type selected.");
          return;
      }
  
      const baseUrl = "http://127.0.0.1:8000"; // Replace with your backend URL
  
      try {
        // Display a loading message while waiting for the response
        resultContainer.textContent = "Loading...";
  
        // Make the API call
        const response = await fetch(baseUrl + endpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(requestBody),
        });
  
        // Check if the response is successful
        if (!response.ok) {
          throw new Error(`API returned status: ${response.status}`);
        }
  
        // Parse and display the plain text result
        const result = await response.text();
        resultContainer.textContent = result;
      } catch (error) {
        console.error("Error:", error);
        resultContainer.textContent = "An error occurred while processing the request.";
      }
    });
  });
  