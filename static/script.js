const generateBtn = document.getElementById("generateBtn");
const emailInput = document.getElementById("emailInput");
const repliesBox = document.getElementById("repliesBox");
const repliesList = document.getElementById("repliesList");
const inputWarning = document.getElementById("inputWarning");
const loader = document.getElementById("loader");

generateBtn.addEventListener("click", async () => {

    const emailText = emailInput.value;

    repliesList.innerHTML = "";
    repliesBox.style.display = "none";

    inputWarning.style.display = "none";

    if (emailText) {
        loader.style.display = "flex";

        try {
            const response = await fetch("http://127.0.0.1:8000/api/generate-replies", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email_text: emailText })
            });

            const data = await response.json();

            data.email_response.forEach(reply => {
                const li = document.createElement("li");
                li.textContent = reply;
                li.onclick = function() {
                    navigator.clipboard.writeText(li.textContent);
                    alert("Texto copiado com sucesso.");
                }
                li.style.cursor = "pointer";
                li.title = "Clique para copiar";

                repliesList.appendChild(li);
            });

            repliesBox.style.display = "flex";
        } catch (err) {
            console.error("Erro:", err);
            loader.style.display = "none";
        }

        loader.style.display = "none";
    } else {
        inputWarning.style.display = "flex";
    }
});