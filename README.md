# 🤖 Discord Bot: Quotes, Weather & Economic News Assistant

This is a simple **Discord bot project** that responds to specific user commands in chat messages.

The bot can return:
- 📜 Inspirational quotes  
- 🌤️ Weather updates  
- 📈 Economic/news summaries  
- 🎲 Random dice rolls  
- 💬 Fun responses and help commands  

---

## 🚀 Features

The bot responds to specific text commands sent in Discord:

### 📜 Quote Command
Returns a daily inspirational quote:

- Quote text  
- Author  
- Source URL  

---

### 🌤️ Weather Command
Returns current weather information including:
- Location (country + city)  
- Date  
- Weather description  
- Temperature (°C)  
- Sunrise time  
- Sunset time  

---

### 📈 Stock / Economic News Command
Returns latest economic/news information:
- News title  
- Snippet  
- Source URL  

---

### 🎲 Dice Roll Command
Returns a random number between **1 and 6**

---

### 💬 Fun Response
If the message contains certain words from a predefined list, the bot responds with a funny reaction.

---

### ❓ Help Command
Displays all available commands and their descriptions.

---

## 📁 Project Structure

```bash id="discord-structure"
discord-bot/
├── main.py        # Discord bot setup and configuration
├── content.py     # Message handling and response logic
├── Quotes.csv     # Dataset for quote generation
