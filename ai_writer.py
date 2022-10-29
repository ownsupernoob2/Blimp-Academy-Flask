import os
import openai
import config
import textwrap as tw
import re
from pprint import pprint

openai.api_key = "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"


def product_observation(prompt_product_desc):
    response = openai.Completion.create(
        model="text-davinci-002",
        # trained responses
        prompt="The following is a conversation with an AI Customer Segment Recommender. \
      The AI is insightful, verbose, and wise, and cares a lot about finding the product market fit.  \
      \n\nHuman: Please state a insightful observation about " + prompt_product_desc,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    pprint(re.split('\n', response.choices[0].text.strip()))

    return response['choices'][0]['text']