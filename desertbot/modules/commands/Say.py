"""
Created on Dec 20, 2011

@author: StarlitGhost
"""
from twisted.plugin import IPlugin
from zope.interface import implementer

from desertbot.message import IRCMessage
from desertbot.moduleinterface import IModule
from desertbot.modules.commandinterface import BotCommand
from desertbot.response import IRCResponse


@implementer(IPlugin, IModule)
class Say(BotCommand):
    def triggers(self):
        return ['say']

    def help(self, query):
        return 'say [channel] <text> - makes the bot repeat the specified text'

    def execute(self, message: IRCMessage):
        if not message.parameterList:
            return IRCResponse('Say what?', message.replyTo)

        if message.parameterList[0] in self.bot.channels:
            return IRCResponse(" ".join(message.parameterList[1:]), message.parameterList[0])

        return IRCResponse(message.parameters, message.replyTo)


say = Say()
