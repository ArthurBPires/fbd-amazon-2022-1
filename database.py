drop_everything_ifexist = """
drop table if exists Oferta_Produto;
drop table if exists Acessa;
drop table if exists Avaliacao;
drop table if exists Carrinho;
drop table if exists Entrega;
drop table if exists Compra;
drop table if exists Mensagem;
drop table if exists Propriedades;
drop table if exists Produto cascade;
drop table if exists Cliente cascade;
drop table if exists Individual;
drop table if exists Profissional;
drop table if exists Vendedor cascade;
drop table if exists Entregador cascade;
drop table if exists Moderador cascade;
drop table if exists Usuario cascade;
drop table if exists Marca cascade;
drop table if exists Categoria cascade;
drop table if exists Local;
drop table if exists Oferta cascade;
drop view if exists ComprasUsuario;
"""
create_tables= """
CREATE TABLE Cliente (
    celular varchar(255),
    pin varchar(255),
    fk_usuario_id int PRIMARY KEY
);
CREATE TABLE Vendedor (
    nome_da_empresa varchar(255) NOT NULL,
    celular varchar(255) UNIQUE NOT NULL,
    cartao_de_credito varchar(255) UNIQUE NOT NULL,
    comissao real NOT NULL,
    cpf_cnpj bigint UNIQUE NOT NULL,
    fk_usuario_id int PRIMARY KEY
);
CREATE TABLE Entregador (
    nome_da_empresa varchar(255) NOT NULL,
    celular varchar(255) UNIQUE NOT NULL,
    cpf_cnpj bigint UNIQUE NOT NULL,
    fk_usuario_id int PRIMARY KEY
);
CREATE TABLE Moderador (
    celular varchar(255) UNIQUE NOT NULL,
    cpf bigint UNIQUE NOT NULL,
    fk_usuario_id int PRIMARY KEY
);
CREATE TABLE Mensagem (
    fk_vendedor_id int NOT NULL,
    fk_cliente_id int NOT NULL,
    fk_moderador_id int,
    lado boolean NOT NULL,
    texto varchar(255) NOT NULL,
    data_hora timestamp NOT NULL,
    denuncia boolean NOT NULL,
    avaliacao boolean,
    acao_tomada varchar(255),
    PRIMARY KEY (fk_vendedor_id, fk_cliente_id, data_hora)
);
CREATE TABLE Individual (
    taxa_p_item real NOT NULL,
    fk_vendedor_id int PRIMARY KEY
);
CREATE TABLE Profissional (
    taxa_mensal real NOT NULL,
    fk_vendedor_id int PRIMARY KEY
);
CREATE TABLE Marca (
    nome varchar(255) PRIMARY KEY
);
CREATE TABLE Categoria (
    nome varchar(255) PRIMARY KEY
);
CREATE TABLE Entrega (
    fk_compra_id int NOT NULL,
    fk_local_id int NOT NULL,
    fk_entregador_id int NOT NULL,
    PRIMARY KEY (fk_compra_id, fk_local_id, fk_entregador_id)
);
CREATE TABLE Compra (
    estado_transacao boolean NOT NULL,
    data_hora timestamp NOT NULL,
    valor real NOT NULL,
    fk_cliente_id int,
    fk_produto_id int,
    quantidade int NOT NULL,
    id int PRIMARY KEY
);
CREATE TABLE Local (
    endereco varchar(255) NOT NULL,
    nome varchar(255) NOT NULL,
    id int PRIMARY KEY,
    descricao varchar(255) NOT NULL
);
CREATE TABLE Oferta (
    valor_percent real NOT NULL,
    descricao varchar(255) NOT NULL,
	data_inicio timestamp NOT NULL,
	data_fim timestamp NOT NULL,
    id int PRIMARY KEY
);
CREATE TABLE Produto (
    descricao varchar(255) NOT NULL,
    preco real NOT NULL,
    nome varchar(255) NOT NULL,
    id int PRIMARY KEY,
    quantidade int NOT NULL,
    fk_vendedor_id int NOT NULL,
    fk_marca_nome varchar(255),
    fk_categoria_nome varchar(255)
);
CREATE TABLE Usuario (
    id int PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    senha varchar(255) NOT NULL,
    nome_titular varchar(255) NOT NULL,
    endereco varchar(255) NOT NULL
);
CREATE TABLE Propriedades (
    fk_produto_id int NOT NULL,
    propriedades varchar(255) NOT NULL,
    PRIMARY KEY (fk_produto_id, propriedades)
);
CREATE TABLE Carrinho (
    fk_produto_id int NOT NULL,
    quantidade int NOT NULL,
    fk_cliente_id int NOT NULL,
    PRIMARY KEY (fk_produto_id, fk_cliente_id)
);
CREATE TABLE Avaliacao (
    fk_produto_id int NOT NULL,
    nota real NOT NULL,
    fk_cliente_id int NOT NULL,
    PRIMARY KEY (fk_produto_id, fk_cliente_id)
);
CREATE TABLE Acessa (
    fk_produto_id int NOT NULL,
    entrada timestamp NOT NULL,
    saida timestamp NOT NULL,
    fk_cliente_id int NOT NULL,
    PRIMARY KEY (fk_produto_id, fk_cliente_id, entrada)
);
CREATE TABLE Oferta_Produto (
    fk_produto_id int NOT NULL,
    fk_oferta_id int NOT NULL,
    PRIMARY KEY (fk_produto_id, fk_oferta_id)
);
"""

alter_tables= """
ALTER TABLE Cliente ADD CONSTRAINT FK_UsuarioCliente
    FOREIGN KEY (fk_usuario_id)
    REFERENCES Usuario (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Vendedor ADD CONSTRAINT FK_UsuarioVendedor
    FOREIGN KEY (fk_usuario_id)
    REFERENCES Usuario (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Entregador ADD CONSTRAINT FK_UsuarioEntregador
    FOREIGN KEY (fk_usuario_id)
    REFERENCES Usuario (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Moderador ADD CONSTRAINT FK_UsuarioModerador
    FOREIGN KEY (fk_usuario_id)
    REFERENCES Usuario (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Mensagem ADD CONSTRAINT FK_ModeradorMensagem
    FOREIGN KEY (fk_moderador_id)
    REFERENCES Moderador (fk_usuario_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
ALTER TABLE Mensagem ADD CONSTRAINT FK_VendedorMensagem
    FOREIGN KEY (fk_vendedor_id)
    REFERENCES Vendedor (fk_usuario_id)
    ON UPDATE CASCADE;
ALTER TABLE Mensagem ADD CONSTRAINT FK_ClienteMensagem
    FOREIGN KEY (fk_cliente_id)
    REFERENCES Cliente (fk_usuario_id)
    ON UPDATE CASCADE;
ALTER TABLE Individual ADD CONSTRAINT FK_VendedorIndividual
    FOREIGN KEY (fk_vendedor_id)
    REFERENCES Vendedor (fk_usuario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Profissional ADD CONSTRAINT FK_VendedorProfissional
    FOREIGN KEY (fk_vendedor_id)
    REFERENCES Vendedor (fk_usuario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Entrega ADD CONSTRAINT FK_LocalEntrega
    FOREIGN KEY (fk_local_id)
    REFERENCES Local (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Entrega ADD CONSTRAINT FK_EntregadorEntrega
    FOREIGN KEY (fk_entregador_id)
    REFERENCES Entregador (fk_usuario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Entrega ADD CONSTRAINT FK_CompraEntrega
    FOREIGN KEY (fk_compra_id)
    REFERENCES Compra (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Compra ADD CONSTRAINT FK_ProdutoCompra
    FOREIGN KEY (fk_produto_id)
    REFERENCES Produto (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
ALTER TABLE Compra ADD CONSTRAINT FK_ClienteCompra
    FOREIGN KEY (fk_cliente_id)
    REFERENCES Cliente (fk_usuario_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
ALTER TABLE Produto ADD CONSTRAINT FK_VendedorProduto
    FOREIGN KEY (fk_vendedor_id)
    REFERENCES Vendedor (fk_usuario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Produto ADD CONSTRAINT FK_MarcaProduto
    FOREIGN KEY (fk_marca_nome)
    REFERENCES marca (nome)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
ALTER TABLE Produto ADD CONSTRAINT FK_CategoriaProduto
    FOREIGN KEY (fk_categoria_nome)
    REFERENCES categoria (nome)
    ON DELETE SET NULL
    ON UPDATE CASCADE;
ALTER TABLE Propriedades ADD CONSTRAINT FK_ProdutoPropriedades
    FOREIGN KEY (fk_produto_id)
    REFERENCES produto (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Carrinho ADD CONSTRAINT FK_ClienteCarrinho
    FOREIGN KEY (fk_cliente_id)
    REFERENCES Cliente (fk_usuario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Carrinho ADD CONSTRAINT FK_ProdutoCarrinho
    FOREIGN KEY (fk_produto_id)
    REFERENCES Produto (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Avaliacao ADD CONSTRAINT FK_ProdutoAvaliacao
    FOREIGN KEY (fk_produto_id)
    REFERENCES Produto (id)
    ON UPDATE CASCADE;
ALTER TABLE Avaliacao ADD CONSTRAINT FK_ClienteAvaliacao
    FOREIGN KEY (fk_cliente_id)
    REFERENCES cliente (fk_usuario_id)
    ON UPDATE CASCADE;
ALTER TABLE Acessa ADD CONSTRAINT FK_ProdutoAcessa
    FOREIGN KEY (fk_produto_id)
    REFERENCES Produto (id)
    ON UPDATE CASCADE;
ALTER TABLE Acessa ADD CONSTRAINT FK_ClienteAcessa
    FOREIGN KEY (fk_cliente_id)
    REFERENCES cliente (fk_usuario_id)
    ON UPDATE CASCADE;
ALTER TABLE Oferta_Produto ADD CONSTRAINT FK_ProdutoOferta_Produto
    FOREIGN KEY (fk_produto_id)
    REFERENCES Produto (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
ALTER TABLE Oferta_Produto ADD CONSTRAINT FK_OfertaOferta_Produto
    FOREIGN KEY (fk_oferta_id)
    REFERENCES Oferta (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
"""