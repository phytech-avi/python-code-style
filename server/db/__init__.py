# Импорт в одну строчку если не превышает количество символов
# в две если импорт разделен логически
# import .db import init_db, get_db #касается db
# import .db import engine #тут получаем другой обьект
from .db import init_db, get_db
