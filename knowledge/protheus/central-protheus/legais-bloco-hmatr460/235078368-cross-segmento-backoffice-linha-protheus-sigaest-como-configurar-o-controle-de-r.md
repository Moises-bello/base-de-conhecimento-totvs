---
article_id: 235078368
category: LEGAIS - BLOCO H/MATR460
content_hash: ac6154630c0850a48cc213edb2ff8b04056e7c3d05eb6710b7063c7e23a6616a
fetched_at: '2026-06-28T22:42:15.052346+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar o
  controle de Rastro para utilizar o FCI?
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078368-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-controle-de-Rastro-para-utilizar-o-FCI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29880173698711) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar o controle de Rastro para utilizar o FCI no Protheus?

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 12.1.17

**Solução**

No **Cadastro de Produtos** (**MATA010**), informe um produto com os seguintes detalhes:

* Campo **Origem** (**B1\_ORIGEM**) indica que produto é de origem estrangeira.
* Campo **Rastro** (**B1\_RASTRO**= **S**; **Rastreabilidade SUBLOTE**): indica a rastreabilidade do produto.

Controle de **SubLote** para produtos novos:

* Pelo módulo **Configurador** o parâmetro **MV\_RASTRO** para conteúdo **S**.
* No cadastro do produto o campo **Rastro** para conteúdo **S**. (B1\_RASTRO= S; Rastreabilidade SUBLOTE)
* Entrada da mercadoria pelo documento de entrada.

Caso queira efetuar controle especifico da numeração do lote informe o campo lote (**D1\_LOTECTL**), caso contrario deixe o campo em branco, o Sistema se encarrega de gerar numeração sequencial par ao lote **AUTOXXXXXX**.

* A movimentação de entrada alimenta o lote nas tabelas **SB8** (**Saldos por lote**) e **SD5** (**Requisições por lote**).

Para utilização de controle de **SubLote** para produtos que já tenham movimentação orientamos alocação de analista, para adequação dos registros na base de dados.

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673)*

*[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-MP-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)*

*[MP - SIGAEST - Validação do Parâmetro MV\_R460TPC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-R460TPC)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
