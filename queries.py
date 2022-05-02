create_view_ComprasUsuario = """
create view ComprasUsuario as
select usuario.id as id_usuario, usuario.nome_titular, usuario.email, usuario.endereco, cliente.celular, compra.estado_transacao, compra.data_hora, compra.valor, compra.quantidade, compra.fk_produto_id
from compra join cliente on compra.fk_cliente_id = cliente.fk_usuario_id join usuario on cliente.fk_usuario_id = usuario.id;
"""

search_discount_category = """
select sum(compra.valor) as valor_total,sum(compra.quantidade) as quantidade_total,categoria.nome as categoria
from produto JOIN compra ON produto.id = compra.fk_produto_id join oferta_produto ON produto.id = oferta_produto.fk_produto_id JOIN oferta ON oferta_produto.fk_oferta_id = oferta.id JOIN categoria ON produto.fk_categoria_nome = categoria.nome
where oferta.valor_percent >= %s and estado_transacao = TRUE and compra.data_hora BETWEEN oferta.data_inicio and oferta.data_fim
GROUP by categoria.nome;
"""

search_company_sold = """
select nome_da_empresa
from vendedor JOIN produto ON vendedor.fk_usuario_id = produto.fk_vendedor_id JOIN compra ON produto.id = compra.fk_produto_id
where compra.estado_transacao = TRUE
GROUP by nome_da_empresa
HAVING SUM(compra.valor) > %s;
"""

search_product_rating = """
select usuario.nome_titular as nome_vendedor
from vendedor JOIN produto ON vendedor.fk_usuario_id = produto.fk_vendedor_id JOIN avaliacao on produto.id = avaliacao.fk_produto_id join usuario on vendedor.fk_usuario_id = usuario.id
GROUP by nome_titular
having MIN(avaliacao.nota) > (select avg(avaliacao.nota)
                              from vendedor JOIN produto ON vendedor.fk_usuario_id = produto.fk_vendedor_id JOIN avaliacao on produto.id = avaliacao.fk_produto_id);
"""

search_most_access = """
select DISTINCT produto.nome,usuario.nome_titular as nome_vendedor
from produto JOIN vendedor ON vendedor.fk_usuario_id = produto.fk_vendedor_id JOIN acessa ON produto.id = acessa.fk_produto_id join usuario on vendedor.fk_usuario_id = usuario.id
group by produto.id,nome_titular
HAVING COUNT(acessa.fk_produto_id) >= all (select count(acessa.fk_produto_id)
                                          from produto JOIN vendedor ON vendedor.fk_usuario_id = produto.fk_vendedor_id JOIN acessa ON produto.id = acessa.fk_produto_id
										  group by produto.id);
"""

search_buyer_profile= """
SELECT DISTINCT usuario.nome_titular,usuario.email
from cliente join usuario on cliente.fk_usuario_id = usuario.id JOIN compra C1 ON cliente.fk_usuario_id = C1.fk_cliente_id
where usuario.id <> %s and not EXISTS (select *
                                            from cliente join usuario on cliente.fk_usuario_id = usuario.id JOIN compra ON cliente.fk_usuario_id = compra.fk_cliente_id
                                            where usuario.id = %s and fk_produto_id not in (select distinct fk_produto_id
                                                                                                 from compra
                                                                                                 where fk_cliente_id = C1.fk_cliente_id));
"""

search_cart = """
select DISTINCT produto.nome,carrinho.quantidade
from cliente join usuario on cliente.fk_usuario_id = usuario.id JOIN carrinho on cliente.fk_usuario_id = carrinho.fk_cliente_id JOIN produto ON carrinho.fk_produto_id = produto.id
where usuario.id = %s;
"""

search_product_seller = """
select DISTINCT comprasusuario.id_usuario,comprasusuario.nome_titular as nome_comprador, comprasusuario.email
from comprasusuario JOIN produto ON comprasusuario.fk_produto_id = produto.id join vendedor on vendedor.fk_usuario_id = produto.fk_vendedor_id join usuario on vendedor.fk_usuario_id = usuario.id
where produto.nome = %s AND usuario.id = %s;
"""

search_product_brand = """
select DISTINCT comprasusuario.nome_titular as nome_comprador
FROM comprasusuario JOIN produto ON comprasusuario.fk_produto_id = produto.id JOIN marca ON produto.fk_marca_nome = marca.nome
WHERE marca.nome = %s;
"""

search_category = """
select AVG(avaliacao.nota) as avaliacao,produto.nome,produto.preco,produto.quantidade,produto.descricao,vendedor.nome_da_empresa as empresa_vendedora,usuario.nome_titular as vendedor
FROM produto LEFT JOIN avaliacao ON produto.id = avaliacao.fk_produto_id JOIN vendedor ON vendedor.fk_usuario_id = produto.fk_vendedor_id join usuario on vendedor.fk_usuario_id = usuario.id JOIN categoria on produto.fk_categoria_nome = categoria.nome
where categoria.nome = %s
GROUP by produto.nome,produto.preco,produto.quantidade,produto.descricao,vendedor.nome_da_empresa,usuario.nome_titular
ORDER BY AVG(avaliacao.nota) DESC;
"""

search_delivery = """
SELECT DISTINCT local.nome as atual_lugar, local.endereco, local.descricao, entregador.nome_da_empresa as empresa_entrega
from compra join entrega ON compra.id = entrega.fk_compra_id join local on entrega.fk_local_id = local.id join entregador on entrega.fk_entregador_id = entregador.fk_usuario_id
where compra.id = %s;
"""