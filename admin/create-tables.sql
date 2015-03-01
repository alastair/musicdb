BEGIN;

-- low level tables

CREATE TABLE audio (
    id          SERIAL,
    path        text not null,
    data        jsonb not null
);

-- primary keys

ALTER TABLE audio ADD CONSTRAINT audio_pkey PRIMARY KEY (id);

-- indexes

-- CREATE INDEX mbid_ndx_lowlevel ON lowlevel (mbid);

COMMIT;
