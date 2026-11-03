---
content_hash: 57f888440f69db7e5b618357151619bb2bbdfbbb9992de372d0b812772953f1a
fetched_at: '2026-06-29T00:10:37.033039+00:00'
page_id: '533751747'
product: rm
source: tdn-rm
title: DT - Validação do Código do Inventário durante inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533751747
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Totvs Gestão de Estoque, Compras e Faturamento |
| Função: | Inventário |
| Ticket: | N/A. |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-10629 |

## **02. SITUAÇÃO/REQUISITO**

Exibir mensagem impedindo de avançar no Assistente de Inclusão de Inventário caso já exista um outro inventário com o mesmo código na coligada corrente.

## **03. SOLUÇÃO**

Foi criado uma nova validação que verifica ao informar o código do inventário à ser criado (no *wizard* Assistente de Inclusão de Inventário) se já existe outro na coligada corrente com o mesmo código (TINVENTARIO.CODINVENTARIO).

Em caso positivo, será apresentado mensagem "Já existe um inventário com o código *xxxxxx*. Informe um novo código para prosseguir!" e o botão Avançar ficará desabilitado até que seja informado um código válido.

Se o código informado não existir na coligada corrente a mensagem não será exibida, o botão Avançar ficará habilitado e o processo de inclusão do inventário poderá ser contiado normalmente.

## **04. DEMAIS INFORMAÇÕES**

Documento de referência:
