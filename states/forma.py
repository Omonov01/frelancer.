from aiogram.dispatcher.filters.state import State,StatesGroup

class adminposition(StatesGroup):
    baseadmin = State()
    reklama = State()
    adv = State()

class personaldata(StatesGroup):
    name = State()
    fullname = State()
    number = State()
    categoriya = State()
    technologies = State()
    yes_no = State()

class emppersonaldata(StatesGroup):
    empname = State()
    empfullname = State()
    empnumber = State()
    empyes_no = State()

class project(StatesGroup):
    projectname = State()
    projectdescription = State()
    projectcost = State()
    projectlink = State()
    projectcategoriya = State()
    projecttechnologies = State()
    projectempyes_no = State()

class userposition(StatesGroup):
    language = State()
    baseposition = State()
    languageposition = State()
    frilansposition = State()
    frilansbalansposition = State()
    frilanssettinsposition = State()
    employeeposition = State()
    employeebalansposition = State()
    employeesettingsposition = State()

