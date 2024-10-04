// Update rendered function in real-time
const functionInput = document.getElementById('function-input');
const renderedFunction = document.getElementById('rendered-function');

function updateRenderedFunction() {
    const input = functionInput.value;
    try {
        // Parse the input expression
        const node = math.parse(input);
        // Convert the parsed expression to LaTeX
        const latex = node.toTex({ parenthesis: 'auto', implicit: 'show' });
        // Render the LaTeX expression
        renderedFunction.innerHTML = '\\(' + latex + '\\)';
        MathJax.typesetPromise();
    } catch (err) {
        // Display an error message
        renderedFunction.innerHTML = '<span style="color: red;">Invalid input</span>';
    }
}

functionInput.addEventListener('input', updateRenderedFunction);

// Insert text at cursor position
function insertText(text) {
    const start = functionInput.selectionStart;
    const end = functionInput.selectionEnd;
    const before = functionInput.value.substring(0, start);
    const after  = functionInput.value.substring(end, functionInput.value.length);
    functionInput.value = before + text + after;
    functionInput.selectionStart = functionInput.selectionEnd = start + text.length;
    functionInput.focus();
    updateRenderedFunction();
}

// Compute derivatives
function computeDerivatives() {
    const functionStr = functionInput.value;
    $.ajax({
        url: '/compute',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ function: functionStr }),
        success: function(response) {
            if (response.success) {
                displayResults(response.results);
            } else {
                alert('Error: ' + response.error);
            }
        }
    });
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    // Define arrays for each type
    const firstPartials = [];
    const secondPurePartials = [];
    const secondMixedPartials = [];

    // Categorize results
    results.forEach(item => {
        if (item.type === 'first') {
            firstPartials.push(item);
        } else if (item.type === 'second_pure') {
            secondPurePartials.push(item);
        } else if (item.type === 'second_mixed') {
            secondMixedPartials.push(item);
        }
    });

    // Function to create and append a heading
    function addHeading(text) {
        const heading = document.createElement('h2');
        heading.textContent = text;
        resultsDiv.appendChild(heading);
    }

    // Function to render a list of items
    function renderItems(items) {
        items.forEach(item => {
            const div = document.createElement('div');
            div.className = 'result-item';
            div.innerHTML = `\\[ ${item.label} = ${item.value} \\]`;
            resultsDiv.appendChild(div);
        });
    }

    // Add headings and render each section
    if (firstPartials.length > 0) {
        addHeading('First Partial Derivatives');
        renderItems(firstPartials);
    }
    if (secondPurePartials.length > 0) {
        addHeading('Second Pure Partial Derivatives');
        renderItems(secondPurePartials);
    }
    if (secondMixedPartials.length > 0) {
        addHeading('Second Mixed Partial Derivatives');
        renderItems(secondMixedPartials);
    }

    MathJax.typesetPromise();
}
