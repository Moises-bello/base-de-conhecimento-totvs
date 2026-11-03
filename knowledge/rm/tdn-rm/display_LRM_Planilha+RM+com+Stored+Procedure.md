---
content_hash: 34659007bb2fcad0fdb17f722fa13535d41c58797eee4bc4162bb6ad3e46a4b0
fetched_at: '2026-06-29T00:05:54.385649+00:00'
page_id: '107938506'
product: rm
source: tdn-rm
title: Planilha RM com Stored Procedure
type: documentation
url: https://tdn.totvs.com/display/LRM/Planilha+RM+com+Stored+Procedure
version: 24
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é demonstrar como criar uma Planilha RM com Stored Procedure.

# Introdução:

---

          As Planilhas RM suportam o uso de Stored Procedure, ou Procedimento Armazenado. Neste documento estão descritos os passos para sua criação.

**Exemplo de Procedure a ser utilizada na Planilha RM**

         Foi criada a procedure abaixo, como exemplo. Veja as funções que são executadas por ela:

CREATE PROCEDURE DBO.XATUALIZA\_SALARIO (@PLN\_Sheet1\_$A1\_S CHAR) AS  
BEGIN  
       /\* VERIFICA SE A TABELA XSALARIO  JÁ EXISTE, E DROPA \*/  
      IF EXISTS  
            ( SELECT     TOP 1 1  
            FROM  SYSOBJECTS  
            WHERE SYSOBJECTS.XTYPE = 'U'  
            AND         SYSOBJECTS.NAME = 'XSALARIO')  
      BEGIN  
            DROP TABLE XSALARIO  
      END

      /\* CRIAÇÃO DA TABELA XSALARIO \*/  
      CREATE TABLE XSALARIO (  
            CHAPA       VARCHAR(10),  
            NOME        VARCHAR(100),  
            SAL\_ANTIGO  FLOAT,  
            SAL\_ATUAL   FLOAT  
      )

                         /\* DADOS PARA PREENCHER A TABELA XSALARIO \*/  
                         INSERT INTO XSALARIO  
                         SELECT      CHAPA, NOME, SALARIO AS SAL\_ANTIGO, (SALARIO \* 1.10) AS SAL\_ATUAL  
                         FROM  PFUNC  
                         WHERE CODSITUACAO <> @PLN\_Sheet1\_$A1\_S

      /\* !!! LEMBRE-SE !!! \*/  
      /\* É NECESSÁRIO UTILIZAR UM COMPONENTE SQL NA PLANILHA RETORNANDO OS DADOS DA TABELA PREENCHIDA PELA PROCEDURE \*/

                         SELECT \* FROM XSALARIO

END

Informações

Lembre-se que na criação de Stored Procedure, a nomenclatura para o parâmetro em SQL é "@" e Oracle é "I", de Inglês.

# Exemplo:

---

           Seguindo os passos abaixo, será possível criar uma Planilha RM com Stored Procedure.

falseExemploPasso 1Passo 1

Após criar a Stored Procedure, temos que cadastrar no sistema RM a sentença SQL que retornará os dados desta Procedure. Para isso, cadastramos a Consulta

SQL com o Código 'Teste\_Procedure'.

Para realizar o cadastro, acesse o menu**'Gestão | Visões de Dados'** e clique no botão Incluir (Ctrl + Ins). Veja a imagem a seguir:

Passo 2Passo 2

Após a criação da Sentença SQL no sistema, vamos criar a planilha RM.

Acesse o menu **'Gestão > Planilha Net'** e clique no botão Incluir (Ctrl + Ins). Em seguida, preencha os campos como ilustrado na imagem abaixo:

Passo 3Passo 3

Após criar a planilha, clique duas vezes sobre ela e será apresentada a sua tela de edição.

Agora, vamos associar a sentença SQL e a procedure na planilha. Selecione a célula da planilha que executará a Consulta SQL e/ou a Procedure.

Em seguida, acesse o menu **'Planilha | Visões de Dados | Associar Consulta SQL à Célula'**.

Passo 4Passo 4

Selecione a **Consulta SQL** e/ou a **Stored Procedure** criadas nos passos anteriores a serem associadas à Planilha RM.

Em seguida, clique no botão 'OK'.

Ao observar a planilha será possível visualizar o resultado, como na figura a seguir:

Passo 5Passo 5

Como mostrado na Procedure, temos a passagem de parâmetros que corresponde a Célula “A1” da planilha. Assim, ao alterar o valor dessa célula para  “A” (Ativos),  e Reexecutar a Consulta SQL, o resultado será atualizado.

Veja as imagens abaixo:

Observação

Para conhecer melhor sobre Planilha RM com Parâmetros das Consultas SQL, visite este .

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Planilha RM

false

**Subprocesso:** Parametrização de Planilha RM com Stored Procedure

falsefalse

**Status:** Finalizado

false

**Data:** 19/07/2016

false

**Autores:**
