from aiogram import Dispatcher, F
from aiogram.filters.command import Command, CommandStart

from handlers.user import command_start, command_consult, get_contact, command_info, command_route, command_services, command_stock


def setup_handlers(dp: Dispatcher) -> None:
    dp.message(CommandStart())(
        command_start
    )
    dp.message(Command("consultation"))(
        command_consult
    )
    dp.message(F.content_type.in_({"contact"}))(
        get_contact
    )
    dp.message(Command("info"))(
        command_info
    )
    dp.message(Command("route"))(
        command_route
    )
    dp.message(Command("services"))(
        command_services
    )
    dp.message(Command("stock"))(
        command_stock
    )
