document.getElementById("generateBtn").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;

    // Call your backend
    const response = await fetch("https://chorded-glendora-uninterpolative.ngrok-free.dev/generate", {
        method: "POST", // or "GET" depending on your backend
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText }) // send inputText if backend expects JSON
    });

    const data = await response.json();
    document.getElementById("output").innerText = JSON.stringify(data);
});
