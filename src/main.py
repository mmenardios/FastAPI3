from fastapi import FastAPI
import json

import os
print(os.getcwd())
 
from src.utils.sentence_prediction import process_sentence, from_str_to_list, tags
from src.utils.model_trained import model_prediction
from src.utils.embedding import use_embed

app = FastAPI()


@app.get("/greet")
async def greet():
    return {"message": "Hello World !"}


@app.post("/predict")
async def prediction(sentence: dict):
    # Turns the json input into a string object
    string_sentence = json.dumps(sentence)

    # process_sentence needs a string objet, and use_embed needs a list object
    processed_sentence = process_sentence(string_sentence)

    # Suppression du premier mot "sentence" de la chaine de caractère
    words = processed_sentence.split(maxsplit=1)
    result_string = words[1]

    list_sentence = from_str_to_list(result_string)

    #embedded_sentence = use_embed(list_sentence)

    #model_output = model_prediction(embedded_sentence)

    #tags_result = tags(model_output)

    #return tags_result
    return "test"
