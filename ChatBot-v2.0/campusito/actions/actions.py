# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionInputTextMensagem(Action):

    def name(self) -> Text:
        return "action_input_text_mensagem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Eu vou lembrar sua mensagem: {text}!")
        return [SlotSet ("name", text)]


class ActionInputTextIdentificacao(Action):

    def name(self) -> Text:
        return "action_input_text_identificacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Eu vou lembrar sua identificação: {text}!")
        return [SlotSet ("name", text)]

        
class ActionInputTextContato(Action):

    def name(self) -> Text:
        return "action_input_text_contato"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Eu vou lembrar seu contato: {text}!")
        return [SlotSet ("name", text)]


