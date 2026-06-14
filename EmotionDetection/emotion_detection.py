import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detecta emociones en un texto usando Watson NLP.
    Retorna un diccionario con las emociones y la emoción dominante.
    
    Args:
        text_to_analyze (str): El texto a analizar
        
    Returns:
        dict: Diccionario con anger, disgust, fear, joy, sadness, dominant_emotion
    """
    # URL del servicio de Watson NLP para detección de emociones
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos por el servicio
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Cuerpo de la solicitud con el texto a analizar
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Enviar solicitud POST al servicio
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convertir el texto de respuesta a diccionario Python
    formatted_response = json.loads(response.text)
    
    # Extraer las emociones del primer prediction
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    
    # Encontrar la emoción dominante (la de mayor puntuación)
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Retornar el diccionario con el formato requerido
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }