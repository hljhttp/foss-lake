from superset.db_engine_specs.base import BaseEngineSpec, LimitMethod


class DremioBaseEngineSpec(BaseEngineSpec):
    engine = "dremio"

    _time_grain_expressions = {
        None: "{col}",
        "PT1S": "DATE_TRUNC('second', {col})",
        "PT1M": "DATE_TRUNC('minute', {col})",
        "PT1H": "DATE_TRUNC('hour', {col})",
        "P1D": "DATE_TRUNC('day', {col})",
        "P1W": "DATE_TRUNC('week', {col})",
        "P1M": "DATE_TRUNC('month', {col})",
        "P0.25Y": "DATE_TRUNC('quarter', {col})",
        "P1Y": "DATE_TRUNC('year', {col})",
    }

    @classmethod
    def epoch_to_dttm(cls) -> str:
        return "TO_DATE({col})"

    @classmethod
    def fetch_data(cls, cursor, limit):
        data = []
        if not cursor.description:
            return []
        if cls.limit_method == LimitMethod.FETCH_MANY:
            for element in cursor.fetchmany(limit):
                row = tuple(list(element))
                data.append(row)
            return data
        else:
            for element in cursor.fetchall():
                row = tuple(list(element))
                data.append(row)
            return data