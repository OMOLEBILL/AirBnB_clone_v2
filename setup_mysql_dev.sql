-- Create a database in hbnb_dev_db and a user hbtn_dv
-- Then grant the user with all privilegdes for this database only
-- the database  should have a SELECT privileges on performance_schema
-- if all above already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
SET FOREIGN_KEY_CHECKS=1;