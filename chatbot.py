print("Ask any question related to my CodSoft Internship.")
print("Type 'exit' to end the chatbot.\n")

while True:
    user = input("user: ").lower().strip()

    if user == "exit":
        print("Chatbot: Thank you! Have a great day.")
        break
    elif user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you?")

    elif "name" in user or "internship" in user:
        print("Chatbot: My internship was with CodSoft as an Artificial Intelligence Intern.")

    elif "duration" in user or "how long" in user:
        print("Chatbot: The internship duration was 4 weeks (1 month).")

    elif "mode" in user or "online" in user or "offline" in user:
        print("Chatbot: The internship was conducted in online mode.")

    elif "objective" in user or "purpose" in user:
        print("Chatbot: The objective was to improve my practical Python programming skills by developing real-world projects.")

    elif "project" in user or "projects" in user:
        print("""Chatbot:
I completed the following projects:
1. AI Chatbot
2. AI Tic-Tac-Toe
3. Recommendation System
4. Face Detection System
5. Image Captioning
""")

    elif "language" in user:
        print("Chatbot: Python was the programming language used throughout the internship.")

    elif "technology" in user or "tools" in user:
        print("""Chatbot:
Technologies Used:
- Python
- OpenCV
- NumPy
- Scikit-learn
- Git & GitHub
- Visual Studio Code
""")

    elif "benefit" in user or "learn" in user or "learning" in user:
        print("""Chatbot:
The internship improved my:
- Python programming skills
- Problem-solving ability
- Debugging skills
- Project development experience
- GitHub knowledge
- Confidence in developing software projects
""")

    elif "challenge" in user or "difficulty" in user:
        print("Chatbot: Initially I faced debugging issues and understanding project logic, but I solved them through practice, documentation, and testing.")

    elif "role" in user:
        print("Chatbot: I independently designed, developed, tested, and documented all the assigned projects.")

    elif "github" in user:
        print("Chatbot: I uploaded all my completed projects to GitHub with proper documentation and README files.")

    elif "why codsoft" in user or "why did you choose codsoft" in user:
        print("Chatbot: I chose CodSoft because it offers project-based learning that helps students gain practical programming experience.")

    elif "future" in user or "plan" in user:
        print("Chatbot: I plan to learn advanced AI, Machine Learning, and Web Development while building more real-world projects.")

    elif "btech" in user or "course" in user:
        print("Chatbot: This internship strengthened the programming and software development skills that support my B.Tech in Artificial Intelligence and Data Science.")

    elif "certificate" in user:
        print("Chatbot: I received a certificate after successfully completing the internship tasks.")

    elif "strength" in user:
        print("Chatbot: My strengths are quick learning, problem-solving, logical thinking, and consistency.")

    elif "weakness" in user:
        print("Chatbot: Initially I took more time to understand complex logic, but continuous practice has improved my confidence.")

    elif user == "how are you?":
                print("Bot: I am fine. Thank you!")
        
    elif user == "what is your name?":
                print("Bot: My name is CodSoft Chatbot.")
        
    elif user == "who created you?":
                print("Bot: I was created using Python.")
        
    elif user == "what is python?":
                print("Bot: Python is a popular programming language.")
        
    elif user == "what is ai?":
                print("Bot: AI stands for Artificial Intelligence.")
        
    elif user == "thank you":
                print("Bot: You're welcome!")
        
    elif user == "bye":
                print("Bot: Goodbye! Have a nice day.")

    else:
            print("Chatbot: Sorry, I don't have an answer for that question. Please ask another internship-related question.")
