FLOAT_TYPES = {"real", "double precision"}

INTEGER_TYPES = {"integer", "smallint", "bigint"}

JSON_TYPES = {"json", "jsonb"}

# https://www.postgresql.org/docs/11/rangetypes.html
RANGE_TYPES = {
    "int4range",  # Range of integer
    "int8range",  # Range of bigint
    "numrange",  # Range of numeric
    "tsrange",  # Range of timestamp without time zone
    "tstzrange",  # Range of timestamp with time zone
    "daterange",  # Range of date
}
