---
content_hash: e83857d2e4b3ab5ec1432b68de1690d1c4bd841cee14a5bb3b4aa86a304d1ebe
fetched_at: '2026-06-29T00:11:17.227185+00:00'
page_id: '677028439'
product: rm
source: tdn-rm
title: Utilizando a atividade "Consulta Sintegra Nacional"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=677028439
version: 8
---

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “Consulta Sintegra Nacional” disponível na Fórmula Visual.

# Especificação:

---

A atividade “Consulta Sintegra Nacional” é uma atividade que permite consultar um CNPJ na base de dados do Sintegra utilizando o serviço disponibilizado pelo [TOTVS API Services - TAS](https://tdn.totvs.com/pages/viewpage.action?pageId=647704528). 

          **Pré requisito**: ter o TOTVS API Services [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=660564412) nos parâmetros globais do sistema.

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | CNPJ | CNPJ a ser consultado | **OBRIGATÓRIO** |
| 2 | Estado | Sigla do Estado. Ex: MG, SP, RJ. | **OBRIGATÓRIO** |

# Acessando o resultado da consulta:

---

Podemos acessar o resultado da consulta através de uma atividade de [expressão](https://tdn.totvs.com/pages/viewpage.action?pageId=161350726), por exemplo:

Adicionando uma atividade [Gerar Exceção](https://tdn.totvs.com/pages/viewpage.action?pageId=149881138) podemos testar a consulta do CNPJ no Sintegra e visualizar o resultado:

Salvando e executando a Fórmula Visual podemos ver o retorno do campo especificado.

O fluxo da Fórmula Visual para teste seria semelhante a este:

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.2205

false

**Processo:** Utilizando atividade "Consulta Sintegra Nacional" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**
