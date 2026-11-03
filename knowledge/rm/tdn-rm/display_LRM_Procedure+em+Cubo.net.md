---
content_hash: 1fa50eaed8722bb702baa1321bc6bad489bb662a6264fd22a1f150dc11dae27c
fetched_at: '2026-06-29T00:11:06.969885+00:00'
page_id: '63865597'
product: rm
source: tdn-rm
title: Procedure em Cubo.net
type: documentation
url: https://tdn.totvs.com/display/LRM/Procedure+em+Cubo.net
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

    Este documento tem por objetivo orientar na criação de cubo .net com a execução de Stored Procedure.

# Execução:

---

    A execução de stored procedure está disponível apenas na versão 11.80, por se tratar de uma sugestão de melhoria.

    Foram realizados os seguintes passos:

    Foi criada uma tabela com o nome Cliente no banco de dados com a seguinte estrutura:

    Feito esse procedimento, foi criada uma stored procedure chamada SPTESTE, conforme abaixo, onde ao executá-la, serão inseridas na tabela Cliente nos campos Codcliente,Nome,CPF,Cidade,UF, passados pelos parâmetros @CODCLIENTE,@NOME,@CPF,@CIDADE,@UF :

    Criadas as tabelas e também a procedure, acessei a nova MDI na versão 11.80, e através do menu  Gestão\Visões de dados, e criei uma consulta SQL com o nome de  SPTESTE, onde  realizei a seguinte consulta

SELECT \* FROM Cliente, conforme abaixo:

    Como não existe registro na tabela, o resultado da consulta não retornou informações:

    Após salvar a consulta, cliquei no botão Configurar\Stored Procedure, aqui no botão  Incluir Nova Stored Porcedure localizei a SPTESTE. Repare que você pode executar a Procedure antes ou depois da execução da consulta SQL, nesse exemplo, optei por executar a SP antes da consulta:

    Ao clicar em Executar, no cadastro da consulta SQL, é aberta a tela de execução da consulta juntamente com os Parâmetros exigidos para a execução da Procedure:

    Ao informar todos e logo após clicar em executar, a Stored Procedure é executada antes da execução da Sentença, conforme configurado acima, alimentando a tabela Cliente:

    Abaixo o resultado da execução da Procedure e após a tabela preenchida:

    Resultado da consulta no Banco:

    Criação do cubo TESTE PROCEDURE já relacionado com a consulta acima criada:

    Ao editar o cubo, como configurei para a Procedure ser executada antes da execução da consulta, é apresentada a tela para passagem dos parâmetros:

    Após executar o processo, configurei o Layout do meu cubo da seguinte forma, repare que a tabela de cliente foi preenchida com os novos parâmetros que passei e o resultado foi exibido juntamente com os registros já existentes na tabela Cliente:

    Resultado consulta no Banco após atualização do cubo:

Só é possível cadastrar uma consulta SQL relacionada com uma Procedure que nela possua parâmetros na versão 11.80. Nas versões anteriores(11.40, 11.50) só é possível associar a uma consulta SQL uma Procedure sem parâmetros.

falsefalse

**Produto:** Framework

false

**Versão:** 11.80

false

**Processo:**Procedure em Cubo .Net

falsefalse

**Status:** Finalizado

false

**Data:**
