// Modern Minimalist UI - JavaScript
// Initialize when DOM is loaded

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the summarization functionality if the elements exist
    initializeSummarization();

    // Set current year in footer
    const yearSpan = document.getElementById('currentYear');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});

// Helper function to display messages in the summary output area
function displaySummaryMessage(outputElement, message, isError = false) {
    const p = document.createElement('p');
    p.textContent = message;
    if (isError) {
        p.className = 'error';
    }
    outputElement.innerHTML = ''; // Clear previous content
    outputElement.appendChild(p);
}
// Function to initialize summarization functionality
function initializeSummarization() {
    const summarizerContainer = document.getElementById('summarizer');
    const inputText = document.getElementById('inputText');
    const summaryLength = document.getElementById('summaryLength');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const summaryOutput = document.getElementById('summaryOutput');
    const loadingIndicator = document.getElementById('loadingIndicator');

    if (summarizerContainer && inputText && summaryLength && summarizeBtn && summaryOutput) {
        const summarizeUrl = summarizerContainer.dataset.summarizeUrl;

        summarizeBtn.addEventListener('click', async function() {
            const text = inputText.value.trim();
            const length = summaryLength.value;

            if (!text) {
                displaySummaryMessage(summaryOutput, 'Please enter some text to summarize.', true);
                return;
            }

            // Show loading indicator and disable button
            loadingIndicator.style.display = 'block';
            summarizeBtn.disabled = true;
            summaryOutput.innerHTML = ''; // Clear previous results
            summaryOutput.classList.add('loading-state');
            
            try {
                const response = await fetch(summarizeUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        text: text,
                        length: length
                    })
                });

                const data = await response.json();

                if (response.ok) {
                    // SECURITY: Use textContent to prevent XSS attacks.
                    displaySummaryMessage(summaryOutput, data.summary);
                } else {
                    displaySummaryMessage(summaryOutput, `Error: ${data.error}`, true);
                }

            } catch (error) {
                displaySummaryMessage(summaryOutput, 'An unexpected network error occurred. Please try again.', true);
            } finally {
                // Hide loading indicator and re-enable button
                loadingIndicator.style.display = 'none';
                summarizeBtn.disabled = false;
                summaryOutput.classList.remove('loading-state');
            }
        });

        // Allow Ctrl+Enter to trigger summarization
        inputText.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                summarizeBtn.click();
            }
        });
    }
}