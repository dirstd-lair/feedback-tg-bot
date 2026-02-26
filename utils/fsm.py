from aiogram.fsm.state import State, StatesGroup

class AppFillingState(StatesGroup):
    title = State()
    description = State()