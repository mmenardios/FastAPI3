import tensorflow_hub as hub
 
#use_loaded_model = hub.load("src/universal_sentence_encoder_model")
module_url = "src/utils/model"
use_loaded_model = hub.load(module_url)
print ("module %s loaded" % use_loaded_model)


def use_embed(input_sentence):
    """
    Fonction créant un embedding de la question de l'utilisateur grâce à un Universal Sentence Encoder
    """
    return use_loaded_model(input_sentence)
