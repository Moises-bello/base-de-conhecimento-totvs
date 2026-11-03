---
content_hash: 0ed20c93467790601efbd12fb3995eaaf4952eaa1dc0da920a706cdc57511f89
fetched_at: '2026-06-29T00:05:55.000294+00:00'
page_id: '118885181'
product: rm
source: tdn-rm
title: Lookup Dependente de Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/Lookup+Dependente+de+Metadados
version: 55
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é exemplificar um LookUp em Metadados para os Itens de outro metadados.

      Veja o  para criar lookup de itens de tabela dinâmica.

# Exemplo

---

     Para este exemplo será necessário criar 3 tabelas de metadados: **Estado, Cidade e Usuário**. O objetivo é fazer um lookup na tela de Cidades, para selecionar o Estado e outro lookup na tela de Usuário para selecionar a Cidade e o Estado.

     Lembramos que para criar esse processo torna-se necessário conhecimento mínimo em como criar um Projeto de Metadados.

falseExemploTabelasTabelasTabelas

**Criaremos as seguinte tabelas:**

**ESTADO**  
ID (Chave Primária)  
ESTADO (Chave Primária, Descrição para Lookup)  
DESCRICAO

**CIDADE**

CODESTADO (Chave Primária)  
CODCIDADE (Chave Primária, Descrição para Lookup)

**USUARIO**  
ID  
NOME  
CODESTADO

Projeto EstadoProjeto EstadoProjeto Estado

**Projeto Estado**

     O projeto **Estado** deverá ser gerado normalmente, passando pelas etapas de um Projeto: *Tabela, Modelo de* *Negócio*, *Apresentação de* *Formulários* e *Projeto:*

Projeto CidadeProjeto CidadeProjeto Cidade

**Projeto Cidade**

     O projeto Cidades receberá o lookup. Após criar a *Tabela*e o *Modelo de Negócio* do projeto **Cidades**, em “Apresentação de Formulários”, preencha as informações da aba Identificação e na aba “**Apresentação**” iremos criar o lookup:

     Selecione o campo que receberá o lookup (no exemplo abaixo **CODESTADO**). Em Tipo de Controle, selecione “Caixa de Pesquisa”.

     Em “Action Fonte de Dados”, selecione o primeiro projeto criado (**Estado**). Obs.: No menu/guia “*Metadados (beta) | Projetos*” pode-se consulta o ID do Projeto **Estado** criado anteriormente. Ou, clique no lookup deste campo e comece a digitar RMSPRJ... para selecionar o projeto Estado.

  Nessa tela é preciso relacionar os campos do lookup e selecionar o campo descrição da fonte de dados.

**Obs.:** Só foi possível utilizar o campo "Estado" na descrição da fonte de dados, porque a opção "Descrição para Lookup" estava marcada na tabela.

     Após estas configurações, gere o projeto **Cidades.**Ele ficará como o exemplo abaixo:

     Concluído e gerado o projeto **CIDADES** com suas informações, iremos criar o último projeto: **USUARIO**.

Projeto UsuárioProjeto UsuárioProjeto Usuário

**Projeto Usuário**

     Semelhante ao projeto **CIDADES**, na etapa de “*Apresentação de Formulários*”, em **USUARIO,** vamos criar um lookup, para as duas tabelas **CODESTADO** e **CODCIDADE**:

     Concluído, basta gerar o projeto e ao executarmos pesquisa por uma cidade deverá retornar somente as cidades pertencentes ao estado da primeira seleção. No exemplo abaixo é listada a cidade de **BELO HORIZONTE** pertencente ao estado de **MINAS GERAIS**.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Lookup Dependente

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
