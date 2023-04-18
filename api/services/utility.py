from datetime import datetime


class UtilityService:
    """Utility Service"""

    @staticmethod
    def generate_response(code, status, message=None):
        """Generates response object"""
        return {
                'code': code,
                'status': status,
                'message': message,
                'date': datetime.now()
            }
