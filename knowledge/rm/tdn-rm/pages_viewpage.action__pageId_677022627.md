---
content_hash: e8980531ff23169724be6abda123fb854326687b22854a2a980132636e42a554
fetched_at: '2026-06-29T00:11:17.215519+00:00'
page_id: '677022627'
product: rm
source: tdn-rm
title: Utilizando a atividade "Consulta Simples Nacional"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=677022627
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “Consulta Simples Nacional” disponível na Fórmula Visual.

# Especificação:

---

A atividade “Consulta Simples Nacional” é uma atividade que permite consultar um CNPJ na base de dados do Simples Nacional utilizando o serviço disponibilizado pelo [TOTVS API Services](https://tdn.totvs.com/pages/viewpage.action?pageId=647704528). 

          **Pré requisito**: ter o TOTVS API Services [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=660564412) nos parâmetros globais do sistema.

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | CNPJ | CNPJ a ser consultado | **OBRIGATÓRIO** |

# Acessando o resultado da consulta:

---

Podemos acessar o resultado da consulta através de uma atividade de [expressão](https://tdn.totvs.com/pages/viewpage.action?pageId=161350726), por exemplo:

Adicionando uma atividade [Gerar Exceção](https://tdn.totvs.com/pages/viewpage.action?pageId=149881138) podemos testar a consulta de CNPJ e visualizar o resultado:

Salvando e executando a Fórmula Visual podemos ver o retorno do campo especificado.

O fluxo da Fórmula Visual para teste seria semelhante a este:

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.2205

false

**Processo:** Utilizando atividade "Consulta Simples Nacional" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**
