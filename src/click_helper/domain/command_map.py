from src.click_helper.handlers import util_handler, log_handler, keyboard_handler, process_handler, mouse_handler

COMMAND_MAP = {
    "WAIT": util_handler.handle_wait,
    "LOG": log_handler.handle_log,
    "HOTKEY": keyboard_handler.handle_hotkey,
    "OPEN_PROCESS": process_handler.handle_open_process,
    "MOVE_TO": mouse_handler.handle_move_to,
    "CLICK": mouse_handler.handle_click,
    "WRITE": keyboard_handler.handle_write,
}