---
content_hash: 43531d4d89d78b01fc5fd8421cec5ff0ddd2f8a156b0a763874a2dd3d155e92c
fetched_at: '2026-06-29T00:11:16.266402+00:00'
page_id: '66617513'
product: rm
source: tdn-rm
title: NF-e - Aproveitamento de ativo imobilizado 1/48 - CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66617513
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.20* |
| **Processo** | **:** | Aproveitamento de ativo imobilizado 1/48 - CIAP |
| **Subprocesso** | **:** | Aproveitamento de ativo imobilizado 1/48 - CIAP |
| **Data da publicação** | **:** | 10/07/2013 |

**Introdução:**

Este documento auxilia na criação de movimento para geração da NF-e para o aproveitamento do ativo imobilizado 1/48.

**Criando uma NF-e de Aproveitamento de Ativo Imobilizado 1/48**

1 - Siga os passos da faq de parametrização de movimento de entrada

 2 -  Selecionar nos parâmetros do Tipo de Movimento a opção  “Emitente / Destinatário”  Empresa

Acesse: Opções / Parâmetros / RM Nucleus / Outras Movimentações / Editar o tipo de movimento / Etapa 2 – Movimento – Emitente e Destinatário

3 - Marcar a opção "Aceitar Preço Zero"

Acesse: Opções / Parâmetros / RM Nuclues / Outras Movimentações / Editar o tipo de movimento / Etapa 27 Item- Preço

4 - Criar um item do tipo produto “Genérico”

Acesse: Cadastro / Produto e Serviços

5 - Criar natureza de operação com o CFOP “1.604” sendo a situação tributária “00 - Tributada Integralmente”, definindo o tipo de ICMS

6 - Selecionar o tipo de movimento onde será criada NF-e de Aproveitamento de 1/48, informar o CFOP na identificação do movimento

7 - Inserir um item com quantidade “1”um e valor “0”zero lembrando que a natureza fiscal deverá ser informada também no item

8 - No tributo do item, informar apenas o valor do ICMS à ser creditado e zerar as outras colunas

O processo de envio da NF-e deverá ser executado normalmente.

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
