import sqlite3

with sqlite3.connect("db.db") as con:
    cur = con.cursor()

    # TABELA MUSICA
    cur.execute('''
        DROP TABLE IF EXISTS musica;
        ''')

    cur.execute(""" CREATE TABLE musica (
                        id	 SERIAL,
                        nome	 VARCHAR(512),
                        autor VARCHAR(512),
                        PRIMARY KEY(id)
                    );
                """)

    # TABELA MOMENTO
    cur.execute('''
        DROP TABLE IF EXISTS momento;
        ''')

    cur.execute(""" CREATE TABLE momento (
                        momento VARCHAR(512),
                        PRIMARY KEY(momento)
                    );
                """)
    
    # TABELA PARTITURA
    cur.execute('''
        DROP TABLE IF EXISTS partitura;
        ''')

    cur.execute(""" CREATE TABLE partitura (
                        path	 VARCHAR(512),
                        musica_id INTEGER NOT NULL,
                        PRIMARY KEY(path),
                        FOREIGN KEY (musica_id) REFERENCES musica(id)
                    );
                """)

    # TABELA MISSA
    cur.execute('''
        DROP TABLE IF EXISTS missa;
        ''')

    cur.execute(""" CREATE TABLE missa (
                        id	 SERIAL,
                        data	 DATE,
                        domingo VARCHAR(512),
                        PRIMARY KEY(id)
                    );
                """)
    
    # TABELA MOMENTO_ESCOLHIDO
    cur.execute('''
        DROP TABLE IF EXISTS momentoescolhido;
        ''')

    cur.execute(""" CREATE TABLE momentoescolhido (
                        momento_nome VARCHAR(512),
                        missa_id   	 INTEGER,
                        musica_id	 INTEGER,
                        PRIMARY KEY(missa_id,musica_id),
                        FOREIGN KEY (missa_id) REFERENCES missa(id),
                        FOREIGN KEY (musica_id) REFERENCES musica(id)
                    );
                """)
    
    # TABELA MUSICA_MOMENTO
    cur.execute('''
        DROP TABLE IF EXISTS musica_momento;
        ''')

    cur.execute(""" CREATE TABLE musica_momento (
                        musica_id	 INTEGER,
                        momento_momento VARCHAR(512),
                        PRIMARY KEY(musica_id,momento_momento),
                        FOREIGN KEY (musica_id) REFERENCES musica(id)
                    );
                """)
    
    # TABELA UTILIZADOR
    cur.execute('''
        DROP TABLE IF EXISTS utilizador;
        ''')

    cur.execute(""" CREATE TABLE utilizador (
                        id	 SERIAL,
                        nome	 VARCHAR(512),
                        password VARCHAR(512),
                        PRIMARY KEY(id)
                    );
                """)
    
    # TABELA UTILIZADOR_MISSA
    cur.execute('''
        DROP TABLE IF EXISTS utilizador_missa;
        ''')

    cur.execute(""" CREATE TABLE utilizador_missa (
                        utilizador_id INTEGER,
                        missa_id	 INTEGER,
                        PRIMARY KEY(utilizador_id,missa_id)
                        FOREIGN KEY (utilizador_id) REFERENCES utilizador(id),
                        FOREIGN KEY (missa_id) REFERENCES missa(id)
                    );
                """)
    
    con.commit()

    
