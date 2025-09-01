import click_helper.handlers.keyboard_handler as keyboard_handler
import click_helper.handlers.log_handler as log_handler
import click_helper.handlers.mouse_handler as mouse_handler
import click_helper.handlers.process_handler as process_handler
import click_helper.handlers.util_handler as util_handler

COMMAND_MAP = {
    "WAIT": util_handler.handle_wait,
    "LOG": log_handler.handle_log,
    "HOTKEY": keyboard_handler.handle_hotkey,
    "OPEN_PROCESS": process_handler.handle_open_process,
    "MOVE_TO": mouse_handler.handle_move_to,
    "CLICK": mouse_handler.handle_click,
    "WRITE": keyboard_handler.handle_write,
}