import sqlite3 as bd


def conectar_bd():
    conn=bd.connect("valquiria_bd")
    curs=conn.cursor()
    return conn, curs


def gerar_cupom():
    n = 0
    try:
        conexao, cursor = conectar_bd()
        cursor.execute("SELECT COUNT(*) FROM vendas WHERE EXISTS (SELECT 1 FROM vendas)") 
        count = cursor.fetchone()[0]
        return count
    except Exception as e:
        print(f'erro{e}')
        return n
    

def lista_de_vendas():
    conexao, cursor = conectar_bd()
    print('n_cupom data_venda       valor_venda           cpf_cliente             cnpj_empresa                  razao_social      operador_vendedor')
    cursor.execute("""
        select n_cupom, data_venda, valor_venda, cpf_cliente, cnpj_empresa, razao_social, operador_vendedor 
        from vendas
    """)
    lista_vendas = cursor.fetchall()
    
    for info_vendas in lista_vendas:
        if info_vendas:
            n_cupom, data_venda, valor_venda, cpf_cliente=info_vendas[0],info_vendas[1],info_vendas[2],info_vendas[3]
            cnpj_empresa, razao_social, operador_vendedor=info_vendas[4],info_vendas[5],info_vendas[6]
            
            print(f'{n_cupom:<2} {data_venda:<12} {valor_venda:<12} {cpf_cliente:<20} {cnpj_empresa:<25} {razao_social:<20} {operador_vendedor:<10}')
    cursor.close()
    conexao.close()


def lista_item_por_carrinho():
    conexao, cursor = conectar_bd()
    cursor.execute("""
                select n_cupom, n_item , plu_produto ,  ean_produto ,  descricao_produto , qtd_produto , preco_unitario , total_preco 
                from carrinho
            """)
    info_carrinho = cursor.fetchall()
    
    if info_carrinho:
        for item in info_carrinho:
            n_cupom, n_item , plu_produto ,  ean_produto ,  descricao_produto = item[0],item[1],item[2],item[3],item[4],
            qtd_produto , preco_unitario , total_preco= item[5],item[6],item[7]

            
            
            print(f'{n_cupom:<8} {n_item:<12} {plu_produto:<10} {ean_produto:<10} {descricao_produto:<15}{qtd_produto:<20}{preco_unitario:<10}{total_preco:>5}')
            
    else:
        print('Não temos nenhum registro de comanda')
    cursor.close()
    conexao.close()


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
                    CREATE TABLE IF NOT EXISTS carrinho (
            n_cupom INTEGER,
            n_item INTEGER, 
            plu_produto TEXT,  
            ean_produto TEXT,  
            descricao_produto TEXT, 
            qtd_produto INTEGER, 
            preco_unitario REAL, 
            total_preco REAL,
            FOREIGN KEY (n_cupom) REFERENCES vendas (n_cupom) )
    """)

    print('tabela carrinho criada')
    conexao, cursor = conectar_bd()
    cursor.execute("""
                        insert into vendas(
                        n_cupom, data_venda, valor_venda, cpf_cliente, cnpj_empresa, razao_social, operador_vendedor)
                        values(?,?,?,?,?,?,?)""",(cupom, data, v_pago, cpf, cnpj, empresa, usuario) )
        
    conexao.commit()
    print("informacoes de cupom inseridas com sucesso")
    
    #inserindo itens
    for compra in carrinho:
                
        cursor.execute("""
                    insert into carrinho(
                    n_cupom, n_item , plu_produto ,  ean_produto ,  descricao_produto , qtd_produto , preco_unitario , total_preco)
                    values(?,?,?,?,?,?,?,?)""",
                    (cupom, compra[0], compra[1], compra[2], compra[3], compra[4], compra[5], compra[6]))
        
        conexao.commit()
        print('Itens iseridos com sucesso')

    cursor.close()
    conexao.close()

   
    lista_de_vendas()
    lista_item_por_carrinho()
    
                
    
        
        
        
    

    
    