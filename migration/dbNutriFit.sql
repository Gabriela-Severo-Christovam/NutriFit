create database dbNutriFit;
use dbNutriFit;

create table tbUsuario (
    email VARCHAR(80) PRIMARY KEY,
    nome VARCHAR (30) NOT NULL,
    telefone VARCHAR(15),
    endereco VARCHAR(80) NOT NULL,
    numero INT NOT NULL,
    senha VARCHAR(100) NOT NULL
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
    url VARCHAR(200)
);


create table tbLogin (
    email VARCHAR(80) PRIMARY KEY,
    senha VARCHAR(8) NOT NULL
);


create table tbCarrinho (
    cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(80),
    cod_produto INT,
    FOREIGN KEY (email) REFERENCES tbUsuario(email),
    FOREIGN KEY (cod_produto) REFERENCES tbProdutos(cod_produto)
   
);

# INSERINDO CATEGORIAS
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

# INSERINDO FOTOS DAS CREATINAS
INSERT INTO tbFotosProdutos (cod_produto, url)
VALUES (1, 'https://www.oceandrop.com.br/media/catalog/product/cache/e72cb892da97e5433e4edef74373290e/6/4/648x908-creatina300_4.png'),
	   (1,'https://www.oceandrop.com.br/media/catalog/product/cache/b8e80b8ab26713fe9633d84839545a38/6/4/648x908-super-box-creatina.png'),
	   (1, 'https://www.oceandrop.com.br/media/catalog/product/cache/b8e80b8ab26713fe9633d84839545a38/6/4/648x908-creatina300-tabela.jpg'),
       (2, 'https://www.gsuplementos.com.br/upload/produto/layout/70/produto1-creapure250-v2.webp'),
       (2, 'https://http2.mlstatic.com/D_NQ_NP_864751-MLB69884251258_062023-O-creatina-250g-creapure-growth-supplements.webp'),
       (2, 'https://a-static.mlcdn.com.br/800x600/omega-3-75-caps-creatina-pura-100g-creapure-growth/maxpowersuplementos/10943820408/f09ee9ba354f7627685592c23da85d26.jpeg');

# INSERINDO FOTOS DOS WHEY
INSERT INTO tbFotosProdutos (cod_produto, url)
VALUES (3, 'https://m.media-amazon.com/images/I/61zXQDYWmcL._AC_SX679_.jpg'),
	   (3, 'https://lojamaxtitanium.vtexassets.com/arquivos/ids/157349/100-whey-protein-max-titanium-dr-peanut-900g-avela-2.jpg?v=638794607032530000'),
       (3, 'https://m.media-amazon.com/images/I/61c5axnIEwL._AC_SX679_.jpg'),
       (4, 'https://sanavita.vtexassets.com/arquivos/ids/157824-1600-auto?v=638736935464570000&width=1600&height=auto&aspect=true');
     
     
# INSERINDO FOTOS PRETREINO
INSERT INTO tbFotosProdutos (cod_produto, url)
VALUES (5, 'https://lojamaxtitanium.vtexassets.com/arquivos/ids/158609-1920-0/MAX-IMAGENS-LANCAMENTOS-TDZ.jpg.jpg?v=638804071627000000'),
	   (6, 'https://http2.mlstatic.com/D_NQ_NP_2X_658224-MLU74927819655_032024-F.webp');
       
# INSERINDO MULTIVITAMINICO
INSERT INTO tbFotosProdutos (cod_produto, url)
VALUES (7, 'https://www.gsuplementos.com.br/upload/produto/layout/107/produto-principal-v2.webp');

# INSERINDO ACESSORIOS
INSERT INTO tbFotosProdutos (cod_produto, url)
VALUES (8, 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQ-3a5nRiZSXAUSo-5_4B4LVpsy6Incp8fW4upm2U6Xrz9w0rFApvure551TC1L9fJMB0RdiF8jfcIBG0jj4UknXAjZTys0OZoqGlEZHK2YpX75qZjqqyndn1E'),
	   (9, 'https://http2.mlstatic.com/D_NQ_NP_2X_726479-MLB69497449602_052023-F-mochila-mala-costas-viagem-transversal-fitness-impermeavel.webp'),
       (10, 'https://www.gsuplementos.com.br/upload/produto/imagem/fita-strap-faixa-preta-growth-manuscrito-par-growth-supplements-1.webp');


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
    ON tbCarrinho.email = tbUsuario.email
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

ALTER TABLE tbComentarios
ADD cod_produto INT,
ADD FOREIGN KEY (cod_produto) REFERENCES tbProdutos(cod_produto);

-- INSERT INTO tbProdutos(nome, descricao, preco, cod_categorias)
-- VALUES ('Whey', 'O melhor do mercado!', 40.90, 2);

-- SELECT * FROM dbnutrifit.tbprodutos;

-- INSERT INTO tbFotosProdutos (cod_produto, url)
-- VALUES (11, 'https://images.tcdn.com.br/img/img_prod/698210/whey_pro_pote_1kg_max_titanium_779_1_79909b369a86c33196f6c741162ec0ab.jpg');