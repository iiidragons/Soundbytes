import openai
import keys

openai.api_key = keys.openai_key
def get_summary(prompt, text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=text
    )
    
    return response.choices[0].text # type: ignore 
def summarize(text, summary_length):
    prompt = f"Summarize this text in {summary_length} sentences for an eleventh-grade student: {text}"
    summary = get_summary(prompt, text)
    return summary

