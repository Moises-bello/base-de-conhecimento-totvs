---
content_hash: bc0cca2705a46cd151f98c5d0c858ea48ba5afcb6fafb0b5ee348a651c235f9e
fetched_at: '2026-06-29T00:10:38.048956+00:00'
page_id: '543083288'
product: rm
source: tdn-rm
title: DT - MDF-e | Nota Técnica 2020.001 - Alteração de Informações do Contratante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543083288
version: 13
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | MDF-e |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-10866 |

## **02. SITUAÇÃO/REQUISITO**

A partir da Nota Técnica 2020.001 de MDF-e, duas novas *tags* passarão a existir dentro do grupo infContratante. São elas: **xNome** e **idEstrangeiro**.

## **03. SOLUÇÃO**

Três campos foram incluídos na tela CTRC Saída, dentro de Movimento | CTRC: **Nome do Contratante, Tipo** e **Estrangeiro?**; sendo o primeiro do tipo *varchar* e com tamanho máximo de 60.

Ao escolher a opção **CIOT**, do grupo **Tipo**, os campos serão alterados para se encaixarem no contexto.

Todos os campos pertencentes à aba 'Informações do Contratante e CIOT' tem sua visibilidade controlada a partir do Código do Modelo do Documento presente no Tipo de documento informado e os valores aceitos são 55 (NF-e) e 57 (CT-e).

## **04. DEMAIS INFORMAÇÕES**

Estes campos **somente serão exibidos** após a execução do script específico para sua criação no banco de dados.
