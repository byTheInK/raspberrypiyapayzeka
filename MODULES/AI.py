from groq import Groq
import json
class Memory:
    def __init__(self, json_file: str):
        self.m_json = json_file
        try:
            with open(self.m_json, 'r+') as f:
                try:
                    data = json.load(f)  # Load JSON data
                except json.JSONDecodeError:
                    data = {}

                if "History" not in data:
                    data["History"] = []

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except FileNotFoundError:
            with open(self.m_json, 'w') as f:
                json.dump({"History": []}, f, indent=4)

        with open(self.m_json, "r+") as f:
            try:
                t = json.load(f)
            except json.JSONDecodeError:
                f.seek(0)
                json.dump({"History": []}, f)
                f.truncate()
                t = {"History": []}
            
            # Ensure "History" key exists
            if "History" not in t:
                t["History"] = []
                f.seek(0)
                json.dump(t, f, indent=4)
                f.truncate()

    def load(self):
        with open(self.m_json, "r") as f:
            return json.load(f)

    def save(self, input_text, output_text):
        with open(self.m_json, "r+") as f:
            data = json.load(f)
            data["History"].append({"user": input_text, "assistant": output_text})
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()


class text:
    def __init__(self,key,memory_json: str, const_data: dict = {"User's name":"Efe","AI's_name":"Mavi Şapkalı"}, max_memory_entries: int = 20):
        self.key = key
        self.const_data = const_data
        self.max_memory_entries = 0 - max_memory_entries
        self.client = Groq(api_key= self.key)
        self.m_json = memory_json

    def createResponseWithData(self, message: str, role: str) -> str:
        m = Memory(self.m_json)
        history = m.load()

        new_history = []

        for entry in history["History"][self.max_memory_entries:]:
            if "user" in entry:
                new_history.append({"role": "user", "content": entry["user"]})
            if "assistant" in entry:
                new_history.append({"role": "assistant", "content": entry["assistant"]})

        new_history.append({"role": role, "content": message})

        for key, value in self.const_data.items():
            new_history.append({"role": "system", "content": f"{key}: {value}"})

        chat_completion = self.client.chat.completions.create(
            messages=new_history,
            model="gemma2-9b-it",
            temperature=0.7,
        )

        response = chat_completion.choices[0].message.content.strip()
        
        m.save(message, response)

        return response


    def createResponse(self, message: str, role: str) -> str:
        chat_completion = self.client.chat.completions.create(
            max_tokens= 2048,
            temperature=0,
            messages=[{"role": role,"content":message}],
            model="gemma2-9b-it",
        )
        return chat_completion.choices[0].message.content