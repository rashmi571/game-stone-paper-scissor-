import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from collections import Counter

class SpamDetectorAI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Spam Detector")
        self.root.geometry("700x650")
        self.root.configure(bg="#1a1a2e")
        
        # Train the AI model with sample data
        self.train_model()
        
        # Title
        title = tk.Label(root, text="🤖 AI SPAM DETECTOR 🤖", 
                        font=("Arial", 26, "bold"), 
                        bg="#1a1a2e", fg="#00d4ff")
        title.pack(pady=20)
        
        # Instruction
        instruction = tk.Label(root, text="Enter your message below to check if it's spam:", 
                              font=("Arial", 12),
                              bg="#1a1a2e", fg="white")
        instruction.pack(pady=5)
        
        # Text input
        input_frame = tk.Frame(root, bg="#1a1a2e")
        input_frame.pack(pady=10, padx=30, fill="both", expand=True)
        
        self.text_input = scrolledtext.ScrolledText(input_frame, 
                                                    font=("Arial", 12),
                                                    wrap=tk.WORD,
                                                    height=10,
                                                    bg="#16213e",
                                                    fg="white",
                                                    insertbackground="white")
        self.text_input.pack(fill="both", expand=True)
        
        # Check button
        check_btn = tk.Button(root, text="🔍 CHECK FOR SPAM",
                             font=("Arial", 14, "bold"),
                             bg="#2ecc71", fg="white",
                             width=25, height=2,
                             bd=0, cursor="hand2",
                             command=self.check_spam)
        check_btn.pack(pady=15)
        
        # Result frame
        result_frame = tk.Frame(root, bg="#16213e", bd=2, relief="solid")
        result_frame.pack(pady=10, padx=30, fill="x")
        
        self.result_label = tk.Label(result_frame, text="Result will appear here", 
                                     font=("Arial", 16, "bold"),
                                     bg="#16213e", fg="white",
                                     pady=20)
        self.result_label.pack()
        
        self.confidence_label = tk.Label(result_frame, text="", 
                                        font=("Arial", 12),
                                        bg="#16213e", fg="#aaaaaa",
                                        pady=5)
        self.confidence_label.pack()
        
        # Clear button
        clear_btn = tk.Button(root, text="🗑️ CLEAR",
                            font=("Arial", 11, "bold"),
                            bg="#e74c3c", fg="white",
                            width=15,
                            bd=0, cursor="hand2",
                            command=self.clear_text)
        clear_btn.pack(pady=10)
        
    def train_model(self):
        """Simple AI training with spam and ham (non-spam) examples"""
        # Spam training data
        self.spam_words = {
            'free', 'win', 'winner', 'cash', 'prize', 'claim', 'urgent',
            'click', 'here', 'now', 'offer', 'limited', 'act', 'bonus',
            'congratulations', 'selected', 'guarantee', 'million', 'dollars',
            'credit', 'loan', 'debt', 'viagra', 'pharmacy', 'pills',
            'weight', 'loss', 'diet', 'enlarge', 'investment', 'profit',
            'make', 'money', 'earn', 'income', 'opportunity', 'business',
            'work', 'home', 'mlm', 'refinance', 'mortgage', 'insurance',
            'lowest', 'rate', 'cheap', 'discount', 'save', 'deal'
        }
        
        # Suspicious patterns
        self.spam_patterns = [
            r'\$\d+',  # Dollar amounts
            r'!!!+',   # Multiple exclamation marks
            r'click here',  # Click here phrases
            r'call now',
            r'\d{3}-\d{3}-\d{4}',  # Phone numbers
            r'100%',
            r'risk[- ]free',
            r'no obligation',
            r'limited time'
        ]
    
    def analyze_text(self, text):
        """AI algorithm to analyze text for spam"""
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        # Count spam words
        spam_word_count = sum(1 for word in words if word in self.spam_words)
        
        # Check for suspicious patterns
        pattern_matches = sum(1 for pattern in self.spam_patterns 
                            if re.search(pattern, text_lower, re.IGNORECASE))
        
        # Check for excessive caps
        caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
        excessive_caps = caps_ratio > 0.3
        
        # Check for excessive punctuation
        excessive_punctuation = text.count('!') > 2 or text.count('?') > 2
        
        # Calculate spam score (0-100)
        spam_score = 0
        spam_score += (spam_word_count / max(len(words), 1)) * 40  # Max 40 points
        spam_score += pattern_matches * 15  # 15 points per pattern
        spam_score += 15 if excessive_caps else 0
        spam_score += 10 if excessive_punctuation else 0
        
        # Cap at 100
        spam_score = min(spam_score, 100)
        
        return spam_score, spam_word_count, pattern_matches
    
    def check_spam(self):
        """Check if the entered text is spam"""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Empty Input", "Please enter some text to check!")
            return
        
        # Analyze the text
        spam_score, spam_words, patterns = self.analyze_text(text)
        
        # Determine result
        if spam_score >= 60:
            result = "⚠️ SPAM DETECTED!"
            color = "#e74c3c"
            verdict = "This message is likely SPAM"
        elif spam_score >= 30:
            result = "⚡ SUSPICIOUS"
            color = "#f39c12"
            verdict = "This message seems suspicious"
        else:
            result = "✅ LOOKS SAFE"
            color = "#2ecc71"
            verdict = "This message appears legitimate"
        
        # Update UI
        self.result_label.config(text=result, fg=color)
        confidence_text = f"{verdict}\nSpam Score: {spam_score:.1f}% | Spam Words: {spam_words} | Patterns: {patterns}"
        self.confidence_label.config(text=confidence_text)
    
    def clear_text(self):
        """Clear the input and results"""
        self.text_input.delete("1.0", tk.END)
        self.result_label.config(text="Result will appear here", fg="white")
        self.confidence_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamDetectorAI(root)
    root.mainloop()