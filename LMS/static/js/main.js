// AI-Powered Cloud LMS - Core Javascript

document.addEventListener("DOMContentLoaded", function () {
    // 1. Sidebar Toggle Logic
    const menuToggle = document.getElementById("menu-toggle");
    const wrapper = document.getElementById("wrapper");

    if (menuToggle && wrapper) {
        menuToggle.addEventListener("click", function (e) {
            e.preventDefault();
            wrapper.classList.toggle("toggled");
        });
    }

    // 2. Auto-dismiss Flash Alerts
    const flashAlerts = document.querySelectorAll(".alert-dismissible");
    flashAlerts.forEach(function (alert) {
        setTimeout(function () {
            // Fade out animation via bootstrap or manual opacity
            alert.style.transition = "opacity 0.6s ease";
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 600);
        }, 4000);
    });

    // 3. AI Assistant Chat Interface Client
    const aiChatForm = document.getElementById("ai-chat-form");
    const aiChatInput = document.getElementById("ai-chat-input");
    const chatHistory = document.getElementById("chat-history");

    if (aiChatForm && aiChatInput && chatHistory) {
        aiChatForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const message = aiChatInput.value.trim();
            if (!message) return;

            // Append Student Message
            appendMessage("user", message);
            aiChatInput.value = "";

            // Append Typing Indicator
            const typingIndicatorId = appendTypingIndicator();
            scrollChatToBottom();

            // Fetch course ID if active
            const courseIdInput = document.getElementById("ai-course-id");
            const courseId = courseIdInput ? courseIdInput.value : "";

            // Send AJAX Request to backend
            fetch("/student/ai_chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    message: message,
                    course_id: courseId
                }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(data => {
                // Remove Typing Indicator
                removeTypingIndicator(typingIndicatorId);
                
                // Append AI Response
                appendMessage("bot", data.response);
                scrollChatToBottom();
            })
            .catch(error => {
                console.error("AI Error:", error);
                removeTypingIndicator(typingIndicatorId);
                appendMessage("bot", "⚠️ Sorry, I encountered a connection error. Please try again.");
                scrollChatToBottom();
            });
        });
    }

    // Helper: Append Chat Bubble
    function appendMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", sender);
        
        // Simple basic markdown to HTML helper (converts linebreaks and bullets/bold)
        messageDiv.innerHTML = formatMarkdown(text);
        
        chatHistory.appendChild(messageDiv);
    }

    // Helper: Append Typing Indicator
    function appendTypingIndicator() {
        const indicatorId = "typing-" + Date.now();
        const indicatorDiv = document.createElement("div");
        indicatorDiv.id = indicatorId;
        indicatorDiv.classList.add("chat-message", "bot");
        indicatorDiv.innerHTML = '<span class="spinner-grow spinner-grow-sm text-primary" role="status"></span> Thinking...';
        chatHistory.appendChild(indicatorDiv);
        return indicatorId;
    }

    // Helper: Remove Typing Indicator
    function removeTypingIndicator(indicatorId) {
        const indicatorDiv = document.getElementById(indicatorId);
        if (indicatorDiv) {
            indicatorDiv.remove();
        }
    }

    // Helper: Scroll Chat Container
    function scrollChatToBottom() {
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    // Helper: Simple Markdown Parser (for bold, bullet points, headers)
    function formatMarkdown(text) {
        // Safe characters
        let html = text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
            
        // Convert headers ### Header
        html = html.replace(/^### (.*$)/gim, '<h5 class="mt-2 text-primary">$1</h5>');
        
        // Convert bold **text**
        html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
        
        // Convert list bullets - Item or * Item
        html = html.replace(/^\s*[-*]\s+(.*$)/gim, '<li>$1</li>');
        
        // Wrap <li> groups in <ul>
        // Very basic wrapper
        if (html.includes("<li>")) {
            // Simple split and recombine check
            const lines = html.split('\n');
            let inList = false;
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].trim().startsWith("<li>")) {
                    if (!inList) {
                        lines[i] = "<ul>" + lines[i];
                        inList = true;
                    }
                } else {
                    if (inList) {
                        lines[i - 1] = lines[i - 1] + "</ul>";
                        inList = false;
                    }
                }
            }
            if (inList) {
                lines[lines.length - 1] = lines[lines.length - 1] + "</ul>";
            }
            html = lines.join('\n');
        }

        // Convert newlines to breaks
        html = html.replace(/\n/g, "<br>");
        
        return html;
    }
});
