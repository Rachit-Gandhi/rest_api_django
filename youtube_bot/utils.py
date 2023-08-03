# youtube_bot/utils.py

# to convert time from seconds into hour:mins:sec format
def seconds_to_hms(time_str):
    seconds = int(time_str)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# to store previous messages in chat and generate an answer to prompts on the basis of history of conversation
def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k", temperature=0):
    import openai
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
