import os
import openai
import config
import textwrap as tw
import re
from pprint import pprint
import key

openai.api_key = key.secret


def product_observation(prompt_product_desc):
    print("Running product observation")
    response = openai.Completion.create(
        model="text-davinci-002",
        # trained responses
        prompt="The following is a conversation with an AI Customer Segment Recommender. \
      The AI is insightful, verbose, and wise, and cares a lot about finding the product market fit.  \
      AI, please state a insightful observation about " + prompt_product_desc + ".",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
        #stop=[" Human:", " AI:"]
    )

    pprint(re.split('\n', response.choices[0].text.strip()))

    return response['choices'][0]['text']

def segment_generator(prompt_product_desc, prompt_seller_persona):
    print("Running Segment Generator")
    response = openai.Completion.create(
        model="text-davinci-002",
        # trained responses
        prompt="The following is a conversation with an AI Customer Segment Recommender. \
        The AI is insightful, verbose, and wise, and cares a lot about finding the product market fit.  \
        What are the top 5 types of customer should a seller who is " + prompt_seller_persona + \
        " sell " + prompt_product_desc + " to?",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )

    pprint(re.split('\n', response.choices[0].text.strip()))

    return response['choices'][0]['text']

def segment_selector(prompt_product_desc, prompt_seller_persona, prompt_focus_segment):
    print("Running Segment Selector")
    response = openai.Completion.create(
        model="text-davinci-002",
        # trained responses
        prompt="The following is a conversation with an AI Customer Segment Recommender. \
        The AI is insightful, verbose, and wise, and cares a lot about finding the product market fit.  \
        What do " + prompt_focus_segment + \
        " look for when buying " + prompt_product_desc + " from "+ prompt_seller_persona + "and where do I typically \
        find " + prompt_focus_segment + "?",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )

    pprint(re.split('\n', response.choices[0].text.strip()))

    return response['choices'][0]['text']
