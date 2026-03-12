from openai import OpenAI

client = OpenAI()

class Brain:

    def think(self, message):
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are JARVIS, John Mwangi's AI assistant."},
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message.content