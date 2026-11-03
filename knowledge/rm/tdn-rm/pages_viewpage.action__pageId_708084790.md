---
content_hash: 679a189074987213b99a4fecc911c0c2b2632d85542e9b9ce1c05abfa40ee6cc
fetched_at: '2026-06-29T00:11:23.186330+00:00'
page_id: '708084790'
product: rm
source: tdn-rm
title: DT FISCAL01-18611 - Erro ao copiar cadastro de Tributo no Fluxus.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708084790
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cópia de tributo |
| País: | Brasil |
| Ticket: | 14948707 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18567 |

## **02. SITUAÇÃO/REQUISITO**

Ao fazer cópia de tributos entre coligadas com natureza orçamentária informada, o sistema está considerando a natureza orçamentária de origem.

## **03. SOLUÇÃO.**

Na cópia de tributos, a coluna CODCOLTBORCAMENTO fica com o mesmo valor da coligada de destino para o tributo copiado.  
Adicionada também validação para, caso a natureza da coligada origem não exista na coligada destino, ela não é copiada com o tributo.

Disponível a partir da versão 12.1.34
