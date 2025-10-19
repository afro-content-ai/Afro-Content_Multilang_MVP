document.getElementById("generateBtn").addEventListener("click", async () => {
    const input = document.getElementById("inputText").value;

    // Call backend API (replace with your endpoint if needed)
    const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input })
    });

    const data = await response.json();
    document.getElementById("output").innerText = data.result || "No output yet.";
});
