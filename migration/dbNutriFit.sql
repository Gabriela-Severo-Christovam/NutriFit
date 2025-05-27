create database dbNutriFit;
use dbNutriFit;

create table tbUsuario (
    email VARCHAR(80),
    nome VARCHAR (30) NOT NULL,
    telefone VARCHAR(10),
    endereco VARCHAR(80) NOT NULL,
    numero INT NOT NULL,
    senha VARCHAR(8) NOT NULL,
    id int PRIMARY KEY
) ;

# AUMENTAR TAMANHO DESCRICAO
create table tbCategoria (
    cod_categorias INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(400)
);

create table tbProdutos (

    nome VARCHAR(80),
    descricao VARCHAR(400),
    preco FLOAT,
    cod_categorias INT,
    cod_produto INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY (cod_categorias) REFERENCES tbCategoria(cod_categorias)
);



create table tbFotosProdutos (
    cod_foto INT AUTO_INCREMENT PRIMARY KEY,
    cod_produto INT,
    FOREIGN KEY (cod_produto) REFERENCES tbProdutos(cod_produto),
    url VARCHAR(80)
);


create table tbLogin (
    email VARCHAR(80) PRIMARY KEY,
    senha VARCHAR(8) NOT NULL
);


create table tbCarrinho (
    cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    id INT,
    cod_produto INT,
    FOREIGN KEY (id) REFERENCES tbUsuario(id),
    FOREIGN KEY (cod_produto) REFERENCES tbProdutos(cod_produto)
   
);


INSERT INTO tbCategoria (descricao)
VALUES ('CREATINA'),
       ('WHEY'),
       ('MUTIVITAMINICO'),
       ('PRÉ-TREINO'),
       ('ACESSÓRIOS')
;



# Produtos com fotos dos produtos
SELECT
    tbProdutos.nome AS nome_produto,
    tbProdutos.descricao AS descricao_produto,
    tbProdutos.preco,
    tbFotosProdutos.url AS url_foto
FROM
    tbProdutos
INNER JOIN
    tbFotosProdutos
    ON tbProdutos.cod_produto = tbFotosProdutos.cod_produto;

# INSERINDO PRODUTOS

# INSERINDO CREATINA
INSERT INTO tbProdutos (nome, descricao, preco, cod_categorias)
VALUES ('Creatina OceanDrop', 'A Creatina Ocean Drop é 100% pura, sem aditivos, e ideal para quem busca mais força, energia e rendimento nos treinos. Com alta absorção, auxilia no ganho de massa magra, melhora a performance e acelera a recuperação muscular. Qualidade e eficácia que você sente nos resultados.', 139.00, 1),
	   ('Creatina Monoidratada Growth', 'A Creatina Monohidratada Growth é ideal para quem busca mais força, explosão e resultados nos treinos. Com alta pureza e excelente custo-benefício, ela favorece o ganho de massa muscular, melhora o desempenho físico e contribui para uma recuperação mais rápida. Qualidade de verdade para evoluir de forma consistente.', 109.00, 1);

# INSERINDO WHEY
INSERT INTO tbProdutos (nome, descricao, preco, cod_categorias)
VALUES ('Whey Max Titanium', 'O Whey Max Titanium é um suplemento de alto valor biológico, ideal para quem busca aumento de massa muscular, recuperação rápida e nutrição de qualidade. Com alta concentração de proteínas e excelente absorção, ele entrega os nutrientes que seu corpo precisa para evoluir com performance e segurança.', 126.00, 2),
	   ('Whey Sanavita', 'Com proteína de alta qualidade, baixo teor de açúcares e excelente digestão, o Whey Sanavita é ideal para recuperação muscular e uma rotina saudável, com sabor e leveza.', 278.76, 2);

# INSERINDO PRÉ TREINO
INSERT INTO tbProdutos (nome, descricao, preco, cod_categorias)
VALUES ('Pré-treino Max Titanium', 'Formulado para aumentar sua energia, foco e desempenho, o Pré-Treino Max Titanium é ideal para quem quer treinar com intensidade. Combina ingredientes potentes que elevam a performance desde a primeira dose.', 145.40, 4),
	   ('Pré-treino Viking Valhalla', 'Pré-treino de alta potência para quem busca energia, concentração e desempenho máximo. Treine como um verdadeiro guerreiro!', 111.81, 4);

# INSERINDO MULTIVITAMINICO
INSERT INTO tbProdutos(nome, descricao, preco, cod_categorias)
VALUES ('Multivitamínico Growth', 'Completo e equilibrado, o Multivitamínico Growth oferece vitaminas e minerais essenciais para fortalecer a imunidade, melhorar o desempenho e manter o corpo em equilíbrio todos os dias.', 47.90, 3);

# INSERINDO ACESSORIOS
INSERT INTO tbProdutos(nome, descricao, preco, cod_categorias)
VALUES ('Blender - Transparente', 'Com design transparente e moderno, a blender é ideal para preparar e consumir seus shakes e suplementos. Leve, resistente e fácil de limpar, é perfeita para o dia a dia na academia ou onde você estiver.', 70.90, 5),
	   ('Bolsa para treino', 'Funcional e resistente, a bolsa de treino oferece espaço ideal para roupas, tênis e acessórios. Com design moderno e compartimentos práticos, é perfeita para acompanhar você na academia, no esporte ou no dia a dia.', 100.00, 5),
	   ('Fita Strap', 'A strap oferece firmeza e proteção para punhos ou articulações, ajudando a prevenir lesões e melhorar a performance em exercícios de força. Confortável e resistente, é essencial para treinos mais intensos.', 19.90, 5);


# Carrinho com usuario e produto
SELECT
    tbUsuario.nome AS nome_usuario,
    tbUsuario.email AS email_usuario,
    tbProdutos.nome AS nome_produto,
    tbProdutos.descricao AS descricao_produto,
    tbProdutos.preco
FROM
    tbCarrinho
INNER JOIN
    tbUsuario
    ON tbCarrinho.id = tbUsuario.id
INNER JOIN
    tbProdutos
    ON tbCarrinho.cod_produto = tbProdutos.cod_produto;


# Produto com Categoria
SELECT
    tbProdutos.nome AS nome_produto,
    tbProdutos.descricao AS descricao_produto,
    tbProdutos.preco,
    tbCategoria.descricao AS categoria_produto
FROM
    tbProdutos
INNER JOIN
    tbCategoria
    ON tbProdutos.cod_categorias = tbCategoria.cod_categorias;


create table tbComentarios (
    nome VARCHAR(80),
    data_hora datetime,
    comentario VARCHAR (400),
    cod_comentario int auto_increment PRIMARY KEY,
    curtidas int
);