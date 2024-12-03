import json
from mojo import context
from db.db_setup import db_setup_init
from db.db_zones import db_zones_init

# main function
if __name__ == "__main__":
    # start db
    db_setup_init()
    db_zones_init()
    
    context.run(globals())
