import os
import google.generativeai as genai
from config import settings


genai.configure(api_key=settings.API_KEY)


from google.generativeai.types import GenerationConfig

# writing the class structure for llm
class GeminiLLM:
    def __init__(self, model, system_prompt: str):
        self.model = model
        self.system_prompt = system_prompt
# Formatting the input
    def predict(self, user_message: str) -> str:
        prompt = (
            self.system_prompt.strip()
            + "\n\nINPUT JSON:\n"
            + user_message
            + "\n\nOUTPUT JSON:"
        )
# Optimising the output according to our needs
        response = self.model.generate_content(
            prompt,
            generation_config=GenerationConfig(
                temperature=0.1,
                max_output_tokens=10000
               
            )
        )

        return response.text.strip()

if __name__ == "__main__":
    print("")