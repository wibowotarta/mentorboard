# === Stage 60: Add saved views for frequently used filters ===
# Project: MentorBoard
class SavedView:
    """Represents a saved filter configuration for MentorBoard views."""
    
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}
    
    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], filters=data.get('filters', {}))
    
    def to_dict(self):
        return {'name': self.name, 'filters': self.filters}


class ViewManager:
    """Manages saved views and applies them to the session tracker."""
    
    PREDEFINED_VIEWS = {
        'active_sessions': {'status': 'Active'},
        'completed_sessions': {'status': 'Completed'},
        'pending_feedback': {'feedback_status': 'Pending'},
        'recent_goals': {'sort_by': 'created_at', 'order': 'desc', 'limit': 10},
        'high_priority': {'priority': 'High'},
    }
    
    def __init__(self):
        self.saved_views = {}
    
    @classmethod
    def get_default_manager(cls):
        return cls()
    
    def add_view(self, name, filters=None):
        if not name or name in self.saved_views:
            raise ValueError("Invalid view name")
        self.saved_views[name] = SavedView(name=name, filters=filters)
    
    def get_saved_view(self, name):
        return self.saved_views.get(name)
    
    def list_all_views(self):
        return list(self.saved_views.values())
    
    def apply_view_to_tracker(self, tracker, view_name):
        saved = self.get_saved_view(view_name)
        if not saved:
            raise ValueError(f"View '{view_name}' not found")
        
        query = QueryBuilder()
        for key, value in saved.filters.items():
            filter_obj = getattr(query, f'add_{key}_filter')()
            if filter_obj and callable(filter_obj):
                filter_obj(value)
        
        return tracker.filter_query(query.build())
    
    def reset_all_views(self):
        self.saved_views.clear()


if __name__ == "__main__":
    vm = ViewManager.get_default_manager()
    vm.add_view('my_active', {'status': 'Active'})
    print(vm.list_all_views())
