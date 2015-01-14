import CommandRouter
import Handler

handler1 = Handler.handler()
handler2 = Handler.handler()
handler3 = Handler.handler()

router = CommandRouter.commandRouter()

router.registerHandler("1", handler1)
router.registerHandler("1", handler2)
router.registerHandler("2", handler3)

router.handle("1", "what1")
router.handle("2", "handler2is pretty sweet")
router.handle("3", "what dat mouf do?")