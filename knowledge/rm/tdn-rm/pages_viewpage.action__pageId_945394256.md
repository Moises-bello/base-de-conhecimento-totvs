---
content_hash: 30c48ca3d1520b7848f455d7d203d01b63d0534245c849f6c3f541c7c7361351
fetched_at: '2026-06-29T00:12:09.350262+00:00'
page_id: '945394256'
product: rm
source: tdn-rm
title: FISCAL01-25402 - Portal de Documentos - O usuário logado não possui privilégios
  suficientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945394256
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Estoque, compras e Faturamento |
| Função: | Painel de Documentos Eletrônicos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25402 |

## **02. SITUAÇÃO/REQUISITO**

Ao tentar acessar o Painel de Documentos Eletrônicos está sendo retornada a mensagem de que o usuário não tem privilégios suficientes para acessar.

## **03. SOLUÇÃO**

Foi atualizado o código de permissão do painel de documentos eletrônicos para permitir que usuários com permissão apenas do gestão de estoque possam acessar o   
Painel de Documentos Eletrônicos sem necessidade de atribuir permissões do Gestão Fiscal.

Disponível a partir da biblioteca 12.1.2406
