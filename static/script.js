function paraphraseText() {
    let inputText = document.getElementById("input-text").value;
    
    fetch('/paraphrase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output-text").innerText = data.paraphrased;
    })
    .catch(error => console.error('Error:', error));
}
