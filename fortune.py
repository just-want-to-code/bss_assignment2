import random

def main():
    print("🔮 Welcome to Subhrajit Mukherjee's Fortune Teller (21JE0950) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    happy_fortunes = [
        "✨ Your fortune: Great things await you, Subhrajit! Keep smiling. ✨",
        "🌞 Your fortune: Today is your lucky day! Embrace the positivity. 🌞"
    ]
    sad_fortunes = [
        "💫 Your fortune: Tough times don't last, but tough people like you do. 💫",
        "🌧️ Your fortune: Every cloud has a silver lining. Keep going. 🌧️"
    ]
    neutral_fortunes = [
        "🌟 Your fortune: A pleasant surprise is on the horizon. 🌟",
        "🔮 Your fortune: A peaceful and harmonious day is ahead. 🔮"
    ]
    stressed_fortunes = [
        "✨ Your fortune: Take a deep breath, Subhrajit. Peace is near. Don't let stress win today. You've got this! ✨",
        "🌿 Your fortune: Breathe deeply. Calm is coming your way. 🌿"
    ]

    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))
    elif mood == "stressed":
        print(random.choice(stressed_fortunes))
    else:
        print("🤔 Sorry, I don't have a fortune for that mood. Try happy, sad, or neutral.")

if __name__ == "__main__":
    main()
