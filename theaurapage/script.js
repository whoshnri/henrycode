document.addEventListener("DOMContentLoaded", () => {
    console.log("Landing page loaded successfully!");
});

document.addEventListener("DOMContentLoaded", () => {

    // Handle form submission
    const form = document.getElementById("message-form");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const message = document.getElementById("message").value;

        // Create mailto link
        const email = "henrybassey2007@gmail.com";
        const subject = "Inbox from The Aura Page";
        const body = encodeURIComponent(message);
        const mailtoLink = `mailto:${email}?subject=${subject}&body=${body}`;

        // Open mailto link
        window.location.href = mailtoLink;

        // Optional: Clear the textarea after sending
        document.getElementById("message").value = "";
    });
});
