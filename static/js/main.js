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
                
                // Append AI Response with RAG metadata
                appendMessage("bot", data.response, {
                    uses_rag: data.uses_rag,
                    sources: data.sources,
                    confidence: data.confidence,
                    chunks_used: data.chunks_used
                });
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

    // Helper: Append Chat Bubble with RAG metadata support
    function appendMessage(sender, text, metadata = {}) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", sender);
        
        // Simple basic markdown to HTML helper (converts linebreaks and bullets/bold)
        messageDiv.innerHTML = formatMarkdown(text);
        
        // Add RAG source attribution if available
        if (sender === "bot" && metadata.uses_rag && metadata.sources && metadata.sources.length > 0) {
            const sourcesDiv = document.createElement("div");
            sourcesDiv.className = "rag-sources mt-3 p-2 bg-light border-left border-info rounded";
            sourcesDiv.style.borderLeft = "4px solid #0d6efd";
            
            const confidenceBadge = `<span class="badge ${getConfidenceBadgeClass(metadata.confidence)} ms-2">
                <i class="fa-solid fa-lightbulb"></i> ${Math.round(metadata.confidence * 100)}% confident
            </span>`;
            
            sourcesDiv.innerHTML = `<strong class="text-muted" style="font-size: 0.85rem;">
                <i class="fa-solid fa-book"></i> Course Materials Source${metadata.sources.length > 1 ? 's' : ''}: ${confidenceBadge}
            </strong><br>`;
            
            metadata.sources.forEach(source => {
                const pageInfo = source.page ? ` (Page ${source.page})` : '';
                sourcesDiv.innerHTML += `<div style="font-size: 0.85rem; margin-top: 4px; color: #666;">
                    📄 <strong>${source.document}</strong>${pageInfo}
                </div>`;
            });
            
            messageDiv.appendChild(sourcesDiv);
        }
        
        chatHistory.appendChild(messageDiv);
    }
    
    // Helper: Get badge class for confidence score
    function getConfidenceBadgeClass(confidence) {
        if (confidence >= 0.75) return "bg-success-subtle text-success";
        if (confidence >= 0.5) return "bg-info-subtle text-info";
        if (confidence >= 0.3) return "bg-warning-subtle text-warning";
        return "bg-danger-subtle text-danger";
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
