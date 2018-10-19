from mycroft import MycroftSkill, intent_file_handler


class WhoseYourOwner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('owner.your.whose.intent')
    def handle_owner_your_whose(self, message):
        self.speak_dialog('owner.your.whose')


def create_skill():
    return WhoseYourOwner()

