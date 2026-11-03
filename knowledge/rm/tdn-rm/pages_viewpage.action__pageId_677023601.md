---
content_hash: ad1c2c97e1c0d379601e0dfec4995a8ea8822c19d4e3a97e7f2218fd7e02f442
fetched_at: '2026-06-29T00:11:17.222267+00:00'
page_id: '677023601'
product: rm
source: tdn-rm
title: Utilizando a atividade "Consulta Nota Fiscal Eletrônica"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=677023601
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “Consulta Nota Fiscal Eletrônica” disponível na Fórmula Visual.

# Especificação:

---

A atividade “Consulta Nota Fiscal Eletrônica” é uma atividade que permite consultar uma NF-e (Nota fiscal Eletrônica) na base de dados de Receita Federal utilizando o serviço disponibilizado pelo [TOTVS API Services](https://tdn.totvs.com/pages/viewpage.action?pageId=647704528). 

          **Pré requisito**: ter o TOTVS API Services [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=660564412) nos parâmetros globais do sistema.

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | Chave de Acesso | Chave de Acesso da NF-e | **OBRIGATÓRIO** |

# Acessando o resultado da consulta:

---

Podemos acessar o resultado da consulta através de uma atividade de [expressão](https://tdn.totvs.com/pages/viewpage.action?pageId=161350726), por exemplo:

Adicionando uma atividade [Gerar Exceção](https://tdn.totvs.com/pages/viewpage.action?pageId=149881138) podemos testar a consulta à NF-e e visualizar o resultado:

Salvando e executando a Fórmula Visual podemos ver o retorno do campo especificado.

O fluxo da Fórmula Visual para teste seria semelhante a este:

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.2205

false

**Processo:** Utilizando atividade "Consulta Nota Fiscal Eletrônica" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**
