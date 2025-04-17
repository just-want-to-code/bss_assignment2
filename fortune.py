# fortune.py

def main():
    print("🔮 Welcome to Subhrajit Mukherjee's Fortune Teller (21JE0950) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Subhrajit! Keep smiling. ✨")
    elif mood == "sad":
        print("💫 Your fortune: Tough times don't last, but tough people like you do. 💫")
    elif mood == "neutral":
        print("🌟 Your fortune: A pleasant surprise is on the horizon. 🌟")
    else:
        print("🤔 Sorry, I don't have a fortune for that mood. Try happy, sad, or neutral.")

if __name__ == "__main__":
    main()
