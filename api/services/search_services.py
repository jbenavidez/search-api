from typing import List, Dict
from api.models import Provider


class SearchService:
    """Search implementation"""
    @classmethod
    def search(cls, params: any) -> List[Dict]:
        """Search for providers"""
        q = params.get("q")
        includes = params.get("includes")
        excludes = params.get("excludes")
        is_active = params.get("is_active")
        active_contition = [
            is_active is not None,
            is_active in ['true', 'false']
        ]
        # set active flag
        if all(active_contition):
            is_active = True if is_active == "true" else False
        return Provider.search(q, includes, excludes, is_active)
