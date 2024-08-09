import sqlite3 as bd

def conectar_bd():
    conn=bd.connect("valquiria_bd")
    curs=conn.cursor()
    return conn, curs

def arquivo(cupom,data,usuario,cnpj,cpf,v_pago,empresa,carrinho):
    #try:
        conexao, cursor = conectar_bd()
        cursor.execute("""
                        create table if not exists vendas(
                            n_cupom integer primary key,    
                            data_venda text,
                            valor_venda real,
                            cpf_cliente text,
                            cnpj_empresa text,
                            razao_social text,
                            operador_vendedor text)""")
        
        print('tabela vendas criada')
        cursor.execute("""
                        insert into vendas(
                        n_cupom, data_venda, valor_venda, cpf_cliente, cnpj_empresa, razao_social, operador_vendedor)
                        values(?,?,?,?,?,?,?)""",(cupom, data, v_pago, cpf, cnpj, empresa, usuario) )
        
        conexao.commit()
        print("informacoes de cupom inseridas com sucesso")

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS carrinho (
                n_cupom INTEGER,
                n_item INTEGER, 
                plu_produto TEXT,  
                ean_produto TEXT,  
                descricao_produto TEXT, 
                qtd_produto INTEGER, 
                preco_unitario REAL, 
                total_preco REAL,
                FOREIGN KEY (n_cupom) REFERENCES vendas (n_cupom) ON DELETE CASCADE)
        """)

        print('tabela carrinho criada')

        
        

        for compra in carrinho:
            if compra:
                cursor.execute("""
                            insert into carrinho(
                            n_item , plu_produto ,  ean_produto ,  descricao_produto , qtd_produto , preco_unitario , total_preco)
                            values(?,?,?,?,?,?,?)""",
                            (compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6]))
                
                conexao.commit()
        print('Itens iseridos com sucesso')
        cursor.close()
        conexao.close()

    #except Exception as e:
        #print(f'erro em banco de dados {e}')
        