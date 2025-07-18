import keys 

import os
os.environ["GOOGLE_API_KEY"] =  keys.GOOGLEKEY

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             temperature=0.9, 
                             max_output_tokens=100,
                             model_kwargs= { "frequency_penalty": 1.5}
            )
                             

# Use invoke with a list of messages
response = llm.invoke([HumanMessage(content="write a story about Sun. Keep it short")])
print(response.content)
 
