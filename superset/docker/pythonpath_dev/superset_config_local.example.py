LANGUAGES = {
    'pt_BR': {'flag': 'br', 'name': 'Brazil'},
    'en': {'flag': 'us', 'name': 'English'},
    'fr': {'flag': 'fr', 'name': 'French'},
}

BABEL_DEFAULT_LOCALE = 'pt_BR'
BABEL_DEFAULT_TIMEZONE = 'America/Recife'

HTTP_HEADERS = {}
TALISMAN_ENABLED = False
SESSION_COOKIE_SAMESITE = None
ENABLE_CORS = True
ENABLE_PROXY_FIX = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}


EXCEL_EXTENSIONS = {"xlsx", "xls"}
CSV_EXTENSIONS = {"csv", "tsv", "txt"}
COLUMNAR_EXTENSIONS = {"parquet", "zip"}
ALLOWED_EXTENSIONS = {*EXCEL_EXTENSIONS, *CSV_EXTENSIONS, *COLUMNAR_EXTENSIONS}

ENABLE_JAVASCRIPT_CONTROLS = True
DASHBOARD_VIRTUALIZATION = True
ENABLE_EXPLORE_DRAG_AND_DROP = True

DEFAULT_FEATURE_FLAGS = {
    "ENABLE_JAVASCRIPT_CONTROLS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "PUBLIC_ROLE_LIKE_GAMMA": True,
    "ALERT_REPORTS": True,
    "DASHBOARD_RBAC": True,
    "DASHBOARD_VIRTUALIZATION": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ALERTS_ATTACH_REPORTS": True,
    "EMBEDDED_SUPERSET": True,
    "ALLOW_FULL_CSV_EXPORT": False,
    "EMBEDDABLE_CHARTS": True,
    "DRILL_TO_DETAIL": True,
    "DRILL_BY": True,
}

D3_FORMAT = {
    "decimal": ",",
    "thousands": ".",
    "grouping": [3],
    "currency": ["R$", ""],
    "dateTime": "%A, %e de %B de %Y. %X",
    "date": "%d/%m/%Y",
    "time": "%H:%M:%S",
    "periods": ["AM", "PM"],
    "days": ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"],
    "shortDays": ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"],
    "months": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
           "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "shortMonths": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set",
                "Out", "Nov", "Dez"]
}
