from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me one Python interview question and its answer."
)

print(interaction.output_text)