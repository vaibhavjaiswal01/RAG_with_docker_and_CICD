import sys
import traceback
from src.RAG_end_to_end.logger import logging

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.get_error_message(error_message, error_details)

    def get_error_message(self, error_message, error_details):
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in file '{file_name}' at line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message
