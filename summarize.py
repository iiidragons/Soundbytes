import openai

openai.api_key = "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"
def get_summary(prompt, text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=3999- len(prompt),
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

