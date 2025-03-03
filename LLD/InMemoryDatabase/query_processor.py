class QueryProcessor:
    @staticmethod
    def filter_by_value(store, condition):
        return {k: v for k, v in store.items() if condition(v)}
    
    @staticmethod
    def range_query(store, min_val, max_val):
        return {k: v for k, v in store.items() if min_val <= v <= max_val}
