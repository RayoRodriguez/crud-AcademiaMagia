CREATE TABLE magic_academy.magic_affinities
(
    id serial NOT NULL,
    name character varying NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE magic_academy.grimoires
(
    id serial NOT NULL,
    grimoire_name character varying NOT NULL,
    front_name character varying NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE magic_academy.applications
(
    id character varying NOT NULL,
    name character varying NOT NULL,
    last_name character varying NOT NULL,
    "DNI" character varying NOT NULL,
    years integer NOT NULL,
    "magic_affinities-id" integer NOT NULL,
    "grimoires-id" integer,
    is_approved boolean NOT NULL DEFAULT false,
    comments character varying,
    created_by character varying,
    created_at date,
    updated_by character varying,
    updated_at date,
    PRIMARY KEY (id),
    CONSTRAINT "ID_Unique" UNIQUE (id),
    CONSTRAINT "DNI_Unique" UNIQUE ("DNI"),
    CONSTRAINT "FK_applications-magic_affinities" FOREIGN KEY ("magic_affinities-id")
        REFERENCES magic_academy.magic_affinities (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT "FK_applications-grimoires" FOREIGN KEY ("grimoires-id")
        REFERENCES magic_academy.grimoires (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
);
