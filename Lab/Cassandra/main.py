from db.database import Database
from helper.write_a_json import write_a_json as wj

db = Database(client_id='fsUcCUiLaEHJFfKbExIBLuuW',
    client_secret='KZ88Ecpja.mGSYwZ8mUzfroZQEw62LHMhRmrhnS9TqLCi_HZO91qgMxOMyXaogi.bKTWhu-LhLhOTB,cFRNeCCR8w81ICwApxgvwb.,09JS2I1lm6eUrgLdrgKOmizNW',
    keyspace='instagram')

#db.insert_stories(1, "matheusjulidori", "2022-06-17 16:00:00", 8, "image12.jpg", "0mo0d3000000000ns", ["user1"])

db.select_stories()

