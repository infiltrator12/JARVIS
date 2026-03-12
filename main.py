from core.orchestrator import JarvisCore

def main():
    jarvis = JarvisCore()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = jarvis.process(user_input)

        print("Jarvis: ", response)

if __name__ == "__main__":
    main()