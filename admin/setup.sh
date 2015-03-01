#!/bin/sh

# Create the database
createdb -E UNICODE -O alastair musicdb

# Create the tables
psql musicdb < create-tables.sql
