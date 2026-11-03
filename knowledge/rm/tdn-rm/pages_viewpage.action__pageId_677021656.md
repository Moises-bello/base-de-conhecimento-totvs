---
content_hash: f4877251c5bfc6e334cb909b352d9ec8b59cbdb89ed2ee12cc343e9bc04c9d07
fetched_at: '2026-06-29T00:11:17.127446+00:00'
page_id: '677021656'
product: rm
source: tdn-rm
title: Utilizando a atividade "Consulta CPF na Receita Federal"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=677021656
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “Consulta CPF na Receita Federal” disponível na Fórmula Visual.

# Especificação:

---

A atividade “Consulta CPF na Receita Federal” é uma atividade que permite consultar um CPF na base de dados de Receita Federal utilizando o serviço disponibilizado pelo [TOTVS API Services](https://tdn.totvs.com/pages/viewpage.action?pageId=647704528). 

          **Pré requisito**: ter o TOTVS API Services [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=660564412) nos parâmetros globais do sistema.

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | CPF | CPF a ser consultado | **OBRIGATÓRIO** |
| 2 | Data de Nascimento | Data de Nascimento do portador do CPF a ser consultado | **OBRIGATÓRIO** |

# Acessando o resultado da consulta:

---

Podemos acessar o resultado da consulta através de uma atividade de [expressão](https://tdn.totvs.com/pages/viewpage.action?pageId=161350726), por exemplo:

Adicionando uma atividade [Gerar Exceção](https://tdn.totvs.com/pages/viewpage.action?pageId=149881138) podemos testar a consulta de CPF e visualizar o resultado:

Salvando e executando a Fórmula Visual podemos ver o retorno do campo especificado.

O fluxo da Fórmula Visual para teste seria semelhante a este:

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.2205

false

**Processo:** Utilizando atividade "Consulta CPF na Receita Federal" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**
