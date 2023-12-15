
/* Questão 1 -- 1,5
a) Descreva a estrutura da tabela "usuarios".

A tabela usuário possui as seguintes colunas: id_usuario do tipo int, auto incrementada e chave primária,
nome do tipo varchar(50), não aceita valore nulos
email do tipo varchar(50), não podendo ser nulo e deve ser único,
senha do tipo varchar(255), não pode ser nulo
data_cadastro do tipo timestamp.

b) Quais são as chaves primárias e estrangeiras na tabela "amizades"?
Chave primária da tabela amizades : id_amizade
Chaves estrangeiras: id_usuario1 e id_usuario2. Ambas referenciando id_usuario da tabela usuarios

c) Explique por que a tabela "perfis" contém uma chave estrangeira referenciando a tabela "usuarios".

Para associar cada perfil a um usuário específico. 
Isso permite que cada usuário tenha um perfil associado.
*/

/* QUestão 2 -- 1,5
a) Escreva uma instrução SQL para inserir um novo usuário na tabela "usuarios".*/

insert into usuarios(nome,email,senha,data_cadastro) values
('Sophie','sophie@gmail.com','54898496848', '2023-03-20 09:45:00' );
/*
b) Como você adicionaria uma nova postagem à tabela "postagens"? Inclua um exemplo.*/
insert into postagens(id_usuario,texto_postagem,data_postagem) values
(3,'Socorro Deux!', '2023-04-10 15:45:00'); 
/*
c) Insira um novo comentário na tabela "comentarios" referente à postagem de ID 2.
*/
INSERT INTO comentarios (id_usuario, id_postagem, texto_comentario, data_comentario) VALUES
    (2, 1, 'E AE!?', '2023-04-05 10:30:00'); /*

/* Questão 3 -- 1,5
a) Escreva uma consulta para recuperar o nome completo e a descrição do perfil do usuário de ID 3. */
SELECT nome_completo, descricao FROM perfis WHERE id_usuario = 3 ;
/*
b) Recupere todas as postagens feitas pelo usuário de e-mail 'maria@example.com'.*/
SELECT usuarios.email, postagens.texto_postagem
FROM usuarios
INNER JOIN postagens ON usuarios.id_usuario = postagens.id_usuario
WHERE usuarios.email = 'maria@example.com'; 
/*
c) Liste os usuários que têm uma amizade aceita com o usuário de ID 1.
*/
SELECT usuarios.nome
FROM usuarios
INNER JOIN  amizades ON usuarios.id_usuario = amizades.id_usuario2
WHERE amizades.id_usuario1 =1 AND amizades.status = 'aceita';

/* Questão 4 -- 1,5
a) Como você atualizaria a senha do usuário de ID 2?*/
update usuarios
set senha = '12356879'
where id_usuario = 2;

/*
b) Altere a descrição do perfil do usuário de ID 3 para "Eu adoro programar!".*/

update perfis
set descricao = "Eu adoro programar!"
where id_perfil = 3;
/*
c) Atualize o status da amizade entre os usuários de ID 1 e ID 3 para 'aceita'.
*/
update amizades
set status = 'aceita'
where id_usuario1 = 1 and id_usuario2 = 3;


/* Questão 5 -- 1,5
a) Escreva uma instrução SQL para excluir uma postagem específica da tabela "postagens".*/

DELETE FROM postagens WHERE texto_postagem= 'Hoje é um ótimo dia!';

/*
b) Como você excluiria um usuário e seu perfil correspondente da rede social?*/

DELETE FROM usuarios WHERE id_usuario = 2;
DELETE FROM perfis WHERE id_perfil =2;

/*
c) Remova todas as amizades pendentes para o usuário de ID 2.
*/
DELETE FROM amizades WHERE id_usuario1 = 2 OR id_usuario2 = 2 AND status = 'pendente';


/* Questão 6 -- 2,5
Perguntas sobre Usuários e Perfis:

a) Liste o nome, e-mail e data de cadastro de todos os usuários juntamente com seus respectivos perfis (nome completo, cidade, estado). */
#Listar 2 tabelas : inner join 

SELECT usuarios.nome, usuarios.email, usuarios.data_cadastro,perfis.nome_completo,perfis.cidade,perfis.estado
from usuarios
inner join perfis on usuarios.id_usuario = perfis.id_usuario;

/*
b) Quais usuários não têm um perfil associado?*/

SELECT * FROM usuarios WHERE id_usuario NOT IN (SELECT id_usuario FROM perfis );
#selecione todas as colunas da tabela usuários aonde o id_usuario não está na tabela perfis 

select usuarios.*
from  usuarios
left join perfis ON usuarios.id_usuario = perfis.id_usuario
where perfis.id_usuario is null;

/*

Perguntas sobre Postagens e Usuários:

c) Recupere o texto de todas as postagens e o nome do usuário que fez cada postagem. */
# INNNER JOIN: postagens.texto, usuario.nome 

select postagens.texto_postagem, usuarios.nome
from postagens
inner join usuarios on postagens.id_postagem = usuarios.id_usuario;

/*
d) Quais postagens foram feitas por usuários que têm uma amizade aceita? */
#inner join: tabelas: postagens , usuarios

/*

Perguntas sobre Comentários e Usuários:

e) Liste todos os comentários feitos, incluindo o texto do comentário e o nome do usuário que fez cada comentário.*/
#comentarios.texto do comentario e o usuario.nome do usuário */

SELECT comentarios.texto_comentario, usuarios.nome
FROM comentarios
INNER JOIN usuarios ON comentarios.id_comentario = usuarios.id_usuario;
/*
f) Quais usuários não fizeram nenhum comentário? */
SELECT * from usuarios where id_usuario not in (select id_usuario from comentarios);


/*Perguntas sobre Amizades e Perfis (para os dois usuários envolvidos):

g) Mostre as informações sobre todas as amizades, incluindo os nomes e descrições dos dois usuários envolvidos.
 nomes das amizades e descricao dos dois usuários/ usuarios
*/
SELECT u1.nome AS nome_usuario1, p1.descricao AS descricao_usuario1, u2.nome AS nome_usuario2, p2.descricao AS descricao_usuario2 
FROM amizades 
INNER JOIN usuarios u1 ON amizades.id_usuario1 = u1.id_usuario 
INNER JOIN perfis p1 ON u1.id_usuario = p1.id_usuario 
INNER JOIN usuarios u2 ON amizades.id_usuario2 = u2.id_usuario 
INNER JOIN perfis p2 ON u2.id_usuario = p2.id_usuario;


/*
h) Quais usuários não têm amizades registradas na tabela?
*/
# select * from usuarios where id_usuario not in (select id_usuario1 from amizades union select id_usuario2 from amizades );

SELECT usuarios.* 
FROM usuarios 
LEFT JOIN amizades AS amizade1 ON usuarios.id_usuario = amizade1.id_usuario1 
LEFT JOIN amizades AS amizade2 ON usuarios.id_usuario = amizade2.id_usuario2 
WHERE amizade1.id_usuario1 IS NULL AND amizade2.id_usuario2 IS NULL ;



