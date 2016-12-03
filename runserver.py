import db_and_common.model
from db_and_common import app

db_and_common.model.createDB()
app.run(host='0.0.0.0', port=5009, debug=True)
